# Investing Tools

Two standalone, browser-based tools for tracking investment income
and analyzing trade returns. No installation required. Open either
HTML file in any browser and it works. Data saves automatically to
your browser between sessions.

Built to answer two questions every investor asks: "How much passive
income is my portfolio generating?" and "How did that trade actually
perform after fees and taxes?"

---

## Screenshot

<!-- Drag and drop a screenshot here after uploading -->

---

## Tools

### 1. Yield — Income Portfolio Tracker (`income-tracker.html`)

A dividend and bond income tracker with live data lookup via the
Financial Modeling Prep API. Track what your holdings pay you,
when they pay you, and how your income is distributed across the
calendar year.

**Features:**
- **Live ticker lookup** — search by ticker or company name;
  pulls dividend history, frequency, yield, and payment dates
  automatically via FMP API.
- **Portfolio summary** — annual income, monthly average, number
  of holdings, and average portfolio yield at a glance.
- **Income tab** — full holdings list with inline editing of
  shares, dividend per share, frequency, and pay day.
- **Calendar tab** — monthly income breakdown showing which
  holdings pay in which months.
- **Bond Ladder tab** — visual month-by-month bond income
  distribution with bar chart.
- **DRIP toggle** — flag holdings enrolled in dividend
  reinvestment plans.
- **Bring your own API key** — enter your own Financial Modeling
  Prep API key; stored locally in your browser.
- **Auto-saves** — all holdings persist in browser localStorage.

### 2. ROI Calculator (`roi-calculator.html`)

A clean trade return calculator for stocks, ETFs, and other assets.
Enter your buy and sell details and get an instant breakdown of how
a trade performed.

**Features:**
- **Two entry modes** — enter by price per share or by total
  dollar amount invested and received.
- **Full cost accounting** — buy-side fees, sell-side fees,
  and dividends received all factor into the calculation.
- **Holding period** — enter buy and sell dates for automatic
  holding period calculation.
- **Results dashboard** — net gain or loss, total ROI percentage,
  return on cost basis, holding period in days, and annualized
  return.
- **Notes field** — attach a note to any trade calculation.
- **Color-coded results** — green for gains, red for losses.
- **No API required** — fully offline after download.

---

## How to Use

### Income Tracker
1. Download `income-tracker.html` and open it in any modern browser.
2. Enter your Financial Modeling Prep API key when prompted
   (free tier works — sign up at financialmodelingprep.com).
3. Search for a ticker or company name in the search box.
4. Review the populated dividend data and click Add to Portfolio.
5. Adjust shares held as needed.
6. Use the Income, Calendar, and Bond Ladder tabs to explore
   your portfolio income.

### ROI Calculator
1. Download `roi-calculator.html` and open it in any modern browser.
2. Choose your entry mode (per share or total amount).
3. Enter your buy price, sell price, shares, and dates.
4. Add any fees and dividends received.
5. Click Calculate ROI.
6. Results appear instantly below.

---

## Disclaimer

Dividend and yield data is sourced from Financial Modeling Prep
and may not reflect the most recent declared dividends. The income
tracker does not constitute financial advice. The ROI calculator
does not account for tax treatment differences between short-term
and long-term gains — consult a tax professional for trade-specific
tax analysis.

---

## Built With

- HTML, CSS, JavaScript
- No frameworks or dependencies — single files, work offline
- Financial Modeling Prep API (income tracker only — free tier)
- Browser localStorage for data persistence

---

## A Note on How This Was Built

These tools were built collaboratively with Claude (Anthropic's AI).
I defined the requirements, iterated on each version, tested the
outputs against real portfolio data, and drove every decision about
what to build and how. Claude helped with code generation and
iteration. The problem-solving, product thinking, and validation
were mine.

I believe in being transparent about AI-assisted work.

---

## License

This project is licensed under the GNU General Public License v3.0.
See the [LICENSE](LICENSE) file for details.

Free to use and modify. If you distribute a modified version, you
must also make your source code available under the same GPL v3
license.

---

## Author

**Meagan Lapworth**
[linkedin.com/in/meagan-lapworth-smallwinz](https://www.linkedin.com/in/meagan-lapworth-smallwinz)
[github.com/MeaganLapworth](https://github.com/MeaganLapworth)
