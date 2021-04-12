# Fundamental Stock Analysis

## IntrinsicValue
**Summary**

Analyzing the intrinsic value of stocks using various valuation methods and financial ratios. Investors such as Warren Buffet and Benjamin Graham are just a few examples of people who use a fundamental analysis approach to value stocks based upon their intrinsic value.  

Below is about how this app works, and the motivation for this type of automated analyses: Which goes over how to go over fundamental stock analysis like those legendary investors mentioned above. I needed a way to apply the things learned in this course without having to do manual calculations for every single stock to come up with an intrinsic value estimate. Before using this app it is highly reccommend that you take the class on udemy which was referenced earlier in this paragraph.   

If you navigate to Steps 2 and 3, that will explain the fundamental analysis and valuation methods that are provided by the application.

### References
https://www.udemy.com/value-investing-bootcamp-how-to-invest-wisely

## Value Investing Process

### Step 1: Initial Screening

An initial stock screener can be done on Google finance, yahoo finance, or many other tools. There are thousands upon thousands of companies in which you can buy stock. You need to use an initial stock screener to narrow down your search. Use the following filtering criteria to narrow down more specific stocks:

1. Filter for companies with return on equity higher than 15%
Return on equity tells us how efficiently a company uses its assets to generate earnings. The higher the return on equity, the better. This is calculated by:
```math
Net Income / Shareholder’s Equity = Return on Equity
```

2. Filter for companies with a current ratio higher than 2%
If the current ratio is greater than one then the company has the ability to pay it’s short term liabilities with its short term assets, because the company has more short term assets than debt. You want a company with more money than bills to pay. If the ratio is less that one, then the company may be vulnerable against any surprising events in the economy and will be hard for them to pay off their bills. To calculate, it is found in the balance sheet:
```math
Current assets / current liabilities = Current ratio
```

3. Filter for a debt to equity ratio lower than 0.5 or 50%
This ratio indicates how much debt a company is in relation to its shareholder’s equity. High debt levels are a huge warning sign as it relies on debt to finance its growth. If a company has an increasing debt to equity ratio, then the investment may become risky because the company cannot meet its debt obligations. Calculated by:
```math
Long-term debt / Shareholder’s equity = debt to equity ratio 
```
### Step 2: Fundamental Analysis

1. **Are earnings per share stable or growing over time?**
   Earnings per share is the profit that a company makes per share of stock. A growing EPS is better than it decreasing or stable. Calculated by:
   ```math
   Net Income / Shares Outstanding = EPS 
   ```
   
2. **How Price Earnings (PE Ratio) compared to the rest of the industry?**
   P/E ratio is the price that you will pay for the stock per dollar of income. This ratio generally differs greatly per industry. A low P/E ratio compared to other stocks in that industry generally means that the shares are trading at a value. 
   Calculated by:  
   ```math
   Price per Share / Earnings per share = P/E ratio
   ```
   
3. **Are free cash flows stable or increasing over time?**  
   FCF is used for paying debts, dividends, buybacks, or investing on growth for the company. Free cash flow is a very important metric for companies as it is hard for companies to manipulate their free cash flows:
   ```math
   Cash From Operating Activities – Cash From Capital Expenditures.
   ``` 
   
4. **Are cash and cash equivalents stable or increasing over time?**
   Reported on the balance sheet. An increasing value means that there is more cash reserves over time. Even though this metric is decreasing, the company can just be investing the reserve money to improve the business.

5. **Is book value per share steadily growing over time?**
   This shows how much money, you would receive for your shares of stock if the company liquidates, selling all of its assets after paying off its debts. You want to look for companies with increasing book value per share because they are companies that are creating value. To calculate:
   ```math
   Shareholder’s Equity / Shares Outstanding = Book value per share
   ```

6. **Is the net margin stable or growing over time?**
   Net margin is what percent of sales is profit. This figure differs greatly from industry to industry. If a company is able to sustain high profit margins, then the company may have a strong brand name or patented products that competitors can’t compete with. The higher the net margin, the better Calculated by:
   ```math
   Net Income/ Revenue = Net Margin or profit margin
   ```

7. **Has the return on equity been consistently high?**
   Return on equity tells us how efficiently a company uses its assets to generate earnings. The higher the return on equity, the better. This is calculated by:
   ```math
   Net Income / Shareholder’s Equity = Return on Equity
   ```

8. **Has debt-to-equity been consistently low or decreasing?**
   This ratio indicates how much debt a company in relation to its shareholder’s equity. High debt levels are a huge warning sign as it relies on debt to finance its growth. If a company has an increasing debt to equity ratio, then the investment may become risky because the company cannot meet its debt obligations. Calculated by:
   ```math
   Long-term debt / Shareholder’s equity = debt to equity ratio 
   ```

### Step 3: Valuation

In this step, we calculate the intrinsic value of a stock based upon two various methods. The price earnings multiple valuation method and the Discounted Cash flow valuation method.

1. **Price Earnings Multiple Valuation Method**  
   
   In this method, a five-year price target is determined based on historical P/E valuation. We will take three inputs to calculate a five-year price target for the company:  
   Input 1: Find the median P/E ratio over the past five years. In this example, we will use 19.0   
   Input 2: Find the company’s earnings per share over the most recent four quarters. This may be listed as “EPS (ttm)” or earnings per share trailing twelve months on various sites. This is calculated by just adding these four quarter EPS figures together. In this example, we will use $2.00  
   Input 3: Now estimate a value which you expect the company will grow its profit each year for the next five years.  
   You can use analysts’ growth rate percentage. Make sure to use the Margin of Safety principle to give your estimate room for error.  
   For example, if analysts predict that the company’s profit will grow 10% each year, then use a 15-25% margin of safety buffer.  
   This means that your growth rate estimate will be conservative and if we use a 25% margin of safety buffer, we will arrive at a value of 7.5% (10 percent estimated growth rate * (1 – .25 margin of safety))
   Now using the three inputs we can arrive at this formula, for a five-year price target (the exponent represents the number of years):  
   
   ```math
   19 * $2.00 * (1 + .075) ^5 = $54.55 
   ```
   
   This value is what the stock price would be five years from now. To calculate what the stock is worth today, its intrinsic value, we need to discount the five-year price target which gives us the net present value (NPV). 10% is a good discount rate to use because it is equal to the long term historical return of the stock market. It is the minimum rate of return to justify picking a stock over investing in an index fund. To calculate the Net Present Value:
   ```math
   $54.55 / (1 + .10) ^5 = $33.87 
   ``
   This, per the P/E valuation model states that the intrinsic value and NPV of that stock is approximately $33.87. 

2. **Discounted Cash Flow Model (DCF)**
   DCF Model projects future cash flows and discounts them back to the present value; this is a valuation method that estimates the intrinsic value of an investment opportunity. The discount rate represents the riskiness of the company’s capital. You then add up the net present value of the cash flows which is the intrinsic value of the company. 
   Cash flows are generally projected 5-10 years. More mature companies who do not expect as much growth in cash flows, such as Coca-Cola will use a 5-year free cash flow projection. In this example we will use a 5-year DCF model.
   
   i. Calculate the company’s capital expenditures from the last four quarters. Sum, it up. In this example, we will use $7,207  
   ii. Calculate the company’s cash from operating activities. Sum it up. Then in the example, we will use $53,944  
   iii. Take the cash from operating activities and subtract it with the capital expenditures. This will give us free cash flow (FCF)
   ```math
   $53,944 - $7,207 = $46,737
   ```
   
3. Then we decide a growth rate of the company for the next five years. This can be analysts’ estimates or your own estimate. If analysts decide that the company will grow at 15.37% each year for the next five years, then use a 25% margin of safety. This means that the conservative growth rate will be (15.37 * (1 - .25)) = 11.53%. **In this application, the automatic selection option is to have the growth rate at a negative value. All this means is that if the growth rate is negative as shown on the app, the calculation for the growth rate value is as follows. The slope of the line of best fit through all historic cash flows is calculated. A predicted free cash flow value is predicted based on this slope one year into the future. Then the growth rate is the percent change of the most recent free cash flow (ttm) value to the predicted free cash flow value one year into the future.**

4. As a company grows in size it is hard to maintain a high growth rate, so each year, the conservative growth rate will decline by 5% each year.

5. So we take our free cash flow of $46,737 and then we multiply it by the conservative growth rate of 11.53% to get the free cash flow one year from now:
   ```math
   (46737 * 1.1153) = $52,125 FCF for year one.

   ```
   
6. Then we discount this future cash flow value using 10% to get the NPV of the first year’s free cash flow 
    ```math
   $52,125 / (1 + .10)^1 = $47,386 NPV FCF
    ```

7. Then every year after the first year, we apply the growth decline rate of 5%. So calculating the second year free cash flow:
   $52,125 * (1 + (.1153 * (1-.05))) = $52,125 * 1.1095 = $57,834 FCF for year two
   
8. Then we discount this future cash flow value using 10% to get the NPV of the second year free cash flow 
   ```math
   $52,125 / (1 + .10)^2 = $47,386 NPV FCF
   ``
   
9. Continue the process till the year 5 FCF and NPV FCF is calculated.
   
10. Take the value of the year 5 FCF, $76,747.49, then you would need to calculate the terminal value which is the company’s long-term valuation as the company approaches perpetuity.

11. To calculate the terminal value using the Gordon Growth Model you also need to come up with a long-term cash flow growth rate. The long-term growth rate for cash flow in the US economy is around 3%, so we will plug that value in the following formula. 
    Terminal value = projected cash flow for final year (1 + long-term growth rate) / (discount rate - long-term growth rate)
    ```math
    $1,129,284 = $76,747.49 * (1 + .03) / (.1 - .03)
    ```
    
12. Now calculate the net present value of the terminal value. The exponent is the last year that you calculated for the terminal value. 
    ```math
    $1,129,284 / (1 + .1)^5 = $701,196
    ```
    
13. Now find the cash and cash equivalents on the balance sheet, in this example we will use, $41,350. Now find long-term debt balance on the balance sheet, in this example, we will use $16,962.
    
14. Take the following inputs and add (subtract debt though) to get the company value using the DCF model.
    
15. You would then take the company value and then divide it by the number of shares outstanding, which will give you the value of the stock price using the DCF model.