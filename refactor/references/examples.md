# Before / after examples

## Python — report export

### Before
```python
def export_report(user_id, fmt, send):
    conn = psycopg.connect(os.environ["DB_URL"])
    rows = conn.execute("select * from orders where user_id=%s", (user_id,)).fetchall()
    total = 0
    lines = []
    for r in rows:
        if r["status"] != "cancelled":
            amt = r["qty"] * r["price"]
            if r["qty"] >= 10:
                amt = amt * 0.9
            total += amt
            lines.append(f"{r['sku']},{r['qty']},{amt:.2f}")
    if fmt == "csv":
        out = "sku,qty,amount\n" + "\n".join(lines) + f"\nTOTAL,,{total:.2f}"
    else:
        out = json.dumps({"lines": lines, "total": round(total, 2)})
    with open(f"/reports/{user_id}.{fmt}", "w") as f:
        f.write(out)
    if send:
        smtplib.SMTP("mail").sendmail("noreply@x", get_email(user_id), out)
    return total
```

Problems: mixes DB, pricing rules, formatting, file I/O and email; boolean flag `send`; magic
numbers; no breakpoints per step; untestable without a database.

### After
```python
BULK_QUANTITY = 10
BULK_DISCOUNT = 0.9


def export_report(user_id, fmt, send):
    """Export a user's billable orders to a report file and optionally email it."""
    orders = order_store.load_orders(user_id)                    # accessor
    report_lines = build_report_lines(orders)                    # engine
    report_text = format_report(report_lines, fmt)               # engine
    report_store.write_report(user_id, fmt, report_text)         # accessor
    if send:
        mailer.send_report(user_id, report_text)                 # accessor
    return sum_amounts(report_lines)                             # engine


# --- engines (pure) ---

def build_report_lines(orders):
    return [to_report_line(order) for order in orders if is_billable(order)]


def is_billable(order):
    return order.status != "cancelled"


def to_report_line(order):
    return ReportLine(sku=order.sku, qty=order.qty, amount=line_amount(order.qty, order.price))


def line_amount(qty, price):
    gross = qty * price
    return gross * BULK_DISCOUNT if qty >= BULK_QUANTITY else gross


def sum_amounts(lines):
    return sum(line.amount for line in lines)


def format_report(lines, fmt):
    formatters = {"csv": format_csv, "json": format_json}       # open for new formats
    return formatters[fmt](lines, sum_amounts(lines))
```

`format_csv` / `format_json` (omitted) reproduce the original output byte-for-byte, and a
characterization test written before the refactor proves it.

Note the public signature — including the `send` flag — is unchanged (frozen contract). The report
lists "boolean flag argument `send`" as a suggested follow-up: split into `export_report` and
`export_and_email_report` once callers can be updated.

## TypeScript — UI handler

### Before
```ts
async function onSaveClick() {
  const name = (document.getElementById("name") as HTMLInputElement).value.trim();
  const email = (document.getElementById("email") as HTMLInputElement).value.trim();
  if (!name) { document.getElementById("err")!.textContent = "Name required"; return; }
  if (!/^[^@]+@[^@]+$/.test(email)) { document.getElementById("err")!.textContent = "Bad email"; return; }
  const res = await fetch("/api/profile", { method: "PUT", body: JSON.stringify({ name, email }) });
  if (!res.ok) { document.getElementById("err")!.textContent = "Save failed"; return; }
  document.getElementById("err")!.textContent = "";
  document.getElementById("status")!.textContent = "Saved";
}
```

### After
```ts
/** Validate the profile form and save it, showing the outcome to the user. */
async function onSaveClick(): Promise<void> {
  const form = profileView.readForm();                 // accessor (screen)
  const validationError = validateProfile(form);       // engine
  if (validationError) return profileView.showError(validationError);

  const result = await profileApi.save(form);          // accessor (network)
  profileView.showSaveResult(describeSaveResult(result)); // engine → accessor
}

// engine
function validateProfile(form: ProfileForm): string | null {
  if (!form.name) return "Name is required.";
  if (!isEmail(form.email)) return "Enter an email like name@example.com.";
  return null;
}
```

The repeated `document.getElementById(...).textContent = ...` became one `profileView` accessor;
the regex became the `isEmail` helper; error messages now tell the user what to do next.
