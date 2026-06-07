# Yield — Income Portfolio Tracker

A standalone, browser-based dividend and bond income tracker. Looks up
live stock, ETF, and bond data via the Financial Modeling Prep API and
displays your projected annual income, monthly averages, a payment
calendar, and a bond ladder breakdown. Portfolio data saves automatically
to your browser between sessions.

Built to solve a real problem: knowing exactly how much passive income
your portfolio generates, when each payment arrives, and how to visualize
it month by month without paying for a subscription service.

---

## Screenshot

<img width="1892" height="769" alt="Screenshot 2026-06-07 at 10 53 56 AM" src="https://github.com/user-attachments/assets/3859029c-1cd3-48e6-ad79-c9420d86445f" />
<img width="1846" height="829" alt="Screenshot 2026-06-07 at 10 54 26 AM" src="https://github.com/user-attachments/assets/61db0957-2660-4dd2-8aff-addf808947fb" />
<img width="1862" height="788" alt="Screenshot 2026-06-07 at 10 54 34 AM" src="https://github.com/user-attachments/assets/1c4a96af-4781-44b8-ae07-4df084e533db" />
<img width="908" height="818" alt="Screenshot 2026-06-06 at 10 02 02 PM" src="https://github.com/user-attachments/assets/6f04ee7e-3659-4803-9acd-fa1972536678" />

---

## Features

- **Live ticker lookup** — search by ticker symbol or company name;
  pulls current price, dividend per share, yield, payment frequency,
  and pay months from the Financial Modeling Prep API
- **Stock, ETF, and bond support** — handles all three asset types
  with appropriate income calculations for each
- **DRIP toggle** — mark any holding as dividend reinvestment plan
- **Inline editing** — update shares, dividend amount, yield, frequency,
  pay months, and DRIP status on any holding without removing and
  re-adding it
- **Income tab** — bar chart of projected monthly income across all
  holdings with a per-holding breakdown table
- **Payment calendar** — monthly calendar view showing which holdings
  pay on which days, color-coded by ticker, with per-day totals
- **Bond ladder tab** — month-by-month income bars showing bond interest
  and dividend income separately with per-holding chips
- **Export / Import** — save your portfolio to a local JSON backup file
  and restore it at any time; protects against browser data loss
- **Summary strip** — at-a-glance annual income, monthly average,
  holding count, and average portfolio yield
- **Auto-saves** — all holdings persist in browser localStorage between
  sessions
- **Runs locally** — no web hosting required; everything stays on your
  own machine

---

## Requirements

- **Python 3** — used to run the local server
  - Mac: already installed on most Macs; confirm by opening Terminal
    and typing `python3 --version`
  - Windows: download free from [python.org](https://python.org) —
    check "Add Python to PATH" during installation
- **A free Financial Modeling Prep API key** — sign up at
  [financialmodelingprep.com](https://financialmodelingprep.com/developer/docs/)
  — takes about 30 seconds, no credit card required
- **A modern browser** — Chrome recommended

---

## Files

| File | Purpose |
|------|---------|
| `income-tracker.html` | The app — open this in your browser |
| `server.py` | Local Python server — must be running for lookups to work |
| `Start Tracker (Mac).command` | Double-click launcher for Mac |
| `Start Tracker (Windows).bat` | Double-click launcher for Windows |

All four files must be kept in the same folder.

---

## Setup

### Step 1 — Add your API key to server.py

Open `server.py` in any text editor. Near the top, find this line:

```python
FMP_API_KEY = "YOUR_API_KEY_HERE"
```

Replace `YOUR_API_KEY_HERE` with the API key from your Financial
Modeling Prep dashboard. Save the file.

### Step 2 — Give the launcher permission to run (Mac only, one time)

Mac will block the `.command` file from running the first time. To
fix this:

1. Open Terminal (search for it with Cmd+Space)
2. Type `chmod +x ` (with a space after the x — don't press Enter yet)
3. Drag the `Start Tracker (Mac).command` file into the Terminal window
4. Press Enter
5. Nothing will happen — that means it worked

If your Mac still shows an error about developer tools, run this in
Terminal and follow the on-screen prompt:

```
xcode-select --install
```

This installs Python's command line tools and only needs to be done
once.

### Step 3 — Start the tracker

- **Mac:** Right-click `Start Tracker (Mac).command` → Open
- **Windows:** Double-click `Start Tracker (Windows).bat`

A Terminal window will open and your browser will launch automatically
at `http://localhost:8080`. The Terminal window must stay open while
you use the app — you can minimize it.

---

## How to Use

### Adding a holding

1. Click the **Add Holdings** tab
2. Type a ticker symbol (e.g. `AAPL`) or company name (e.g.
   `Vanguard S&P 500`) in the search box
3. Press Enter or click **Look up**
4. Review the data that comes back — yield, dividend per share,
   frequency, and pay months
5. Enter the number of shares you hold
6. Check **Enable DRIP** if you reinvest dividends automatically
7. Click **Add to portfolio**

For stocks not currently paying a dividend, set the yield and
dividend fields to 0 and use the Edit button to update them later
when dividends begin.

### Editing a holding

Click the ✏️ button on any holding to expand an edit panel. You can
update:

- Number of shares
- Dividend per share (per payment)
- Annual yield %
- Payment frequency
- Day of month the payment arrives
- DRIP on/off
- Which months it pays (click the month buttons to toggle)

Click **Save changes** when done or **Cancel** to discard.

### Tabs

- **Income** — bar chart of monthly projected income + breakdown by
  holding
- **Calendar** — monthly calendar with payouts shown on their pay
  dates; navigate forward and backward with the arrows
- **Bond Ladder** — month-by-month ladder view showing bond interest
  and dividend income separately

### Backing up your portfolio

Click **💾 Export** in the My Holdings panel to download a JSON backup
file. Store it somewhere safe such as iCloud Drive or your Documents
folder. To restore, click **📂 Import** and select your backup file.

> **Important:** your portfolio saves in Chrome's local storage. If
> you clear Chrome's cookies and site data, your portfolio will be
> erased. Export a backup regularly to prevent data loss.

---

## API Usage

The free Financial Modeling Prep tier allows 250 API calls per day.
Each ticker lookup uses 2–3 calls (search, profile, dividend history).
For personal use with a modest-sized portfolio this is more than
sufficient.

The API key is stored only in `server.py` on your local machine and
is never exposed in the browser or transmitted anywhere except directly
to the Financial Modeling Prep API.

---

## Disclaimer

Dividend yields, payment dates, and income projections are estimates
based on historical data from the Financial Modeling Prep API.
Actual dividends may differ. Payment dates shown on the calendar are
based on historical pay patterns and may not reflect future declared
dates. This tool is for personal planning and informational purposes
only — not financial advice. Consult a financial advisor before making
investment decisions.

---

## Built With

- HTML, CSS, JavaScript
- Python 3 (local server / API proxy)
- Chart.js 4.4.1 (via CDN)
- Google Fonts — DM Serif Display, DM Sans
- Financial Modeling Prep API (live data)
- Browser localStorage for portfolio persistence

---

## A Note on How This Was Built

This tool was built collaboratively with Claude (Anthropic's AI).
I defined the requirements, identified the data sources, drove every
design and feature decision, tested the app against real portfolio
data, caught errors, and iterated on each version. Claude helped with
code generation and iteration. The problem-solving, product thinking,
and validation were mine.

I believe in being transparent about AI-assisted work.

---

## License

This project is licensed under the GNU General Public License v3.0.
See the [LICENSE](LICENSE) file for details.

Free to use and modify. If you distribute a modified version, you must
also make your source code available under the same GPL v3 license.

---

## Author

**Meagan Lapworth**
[linkedin.com/in/meagan-lapworth-smallwinz](https://www.linkedin.com/in/meagan-lapworth-smallwinz)
[github.com/MeaganLapworth](https://github.com/MeaganLapworth)
