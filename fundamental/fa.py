# Automated Stock Analysis

import numpy as np
import pandas as pd
import matplotlib as plt

# Choose stock tickers to grab data and other parameters
tickers = ["MSFT", "GOOG", "AMZN", "IBM"]

ExpectedGrowthRate = -1
MarginSafety = .10
GrowthDeclineRate = .05
DiscountRate = .09
DCF_YearsProjection = 5
LongTermGrowthRate = .03

# Get the financial statement data of the tickers for the past four years

for ticker in tickers:
    print(ticker)

# Get the stock ticker information
# Create temporary data frames for each of the financial statements
# FinancialStatement = "BalanceSheet"
# FinancialStatement = "IncomeStatement"
# FnancialStatement = "CashFlow"

FinancialStatement = []
BalanceSheet = FinancialStatement[0]
IncomeStatement = FinancialStatement[1]
CashFlow = [2]

# Rebind the data to append ticker information
Ticker = ticker[i]

# Rename some column variables
date = 0
value = 0

# Clean out the Date column

# Get the financial statement data of the tickers for the past four quarters

# Get the stock ticker information

# Create temporary data frames for each of the financial statements

# Melt the data to reshape the date column variables into a value under a single variable

# Rebind the data to append ticker information

# PE Valuation Data Cleansing, past four quarter

# # Get the unique dates for the stock ticker in the financial statements

# Loop to get data for all unique dates in the financial statements

# Check if the date in financial statements is found in the tempPrice_df

# Get the ticker's stock price and append date column
# def get_symbols(ticker, start, end, src='google'):
#     tempPrice_df < data.frame(tempPrice_df)
#     tempPrice_df$Date < rownames(tempPrice_df)
#     rownames(tempPrice_df) < NULL
#     empPrice_df < tempPrice_df[order(tempPrice_df$Date, decreasing = FALSE), ]

# '''
# If the max date of the financial statement does not equal a date in the tempPrice_df, then subtract the Date by 1, then loop till TRUE
# '''
# if (Dates[x] == sort(tempPrice_df$Date)[1]){ tempPrice_df < - cbind(tempPrice_df[1, ],
# # "Ticker"=ticker[i]) colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df)) ClosePriceQtr_df < - rbind(
# # ClosePriceQtr_df, tempPrice_df) check < - TRUE }
# #
# else {
# Dates[x] < - as.character(as.Date(Dates[x]) - 1)

# It is possible that the company was not a publicly traded company during the date on the financial statement, so won't have matching stock price data. Once counter = 5 then stop the program
if counter == 5:
    tempPrice_df = data.frame("Open"="NA", "High"="NA", "Low"="NA", "Close"="NA", "Volume"="NA", "Adjusted"="NA","Date"=unique(temp_data$Date)[x], "Ticker"=ticker[i])
 ClosePriceQtr_df = rbind(ClosePriceQtr_df, tempPrice_df)
check = TRUE

# PE Valuation Data Cleansing for annual data
for ticker in tickers:
    ClosePrice_df = data.frame()

# Get the unique dates for the stock ticker in the financial statements
temp_data = data[data.Ticker == ticker[i], ]
temp_data = temp_data[order(temp_data$Date, decreasing = TRUE), ]
Dates = unique(temp_data.Date)

# Loop to get data for all unique dates in the financial statments
for date in dates:
    pass

# Check if the date in financial statements is found in the tempPrice_df
check = False
counter = 0

while not check:
    counter = counter + 1

# Get the ticker's stock price and append date column
# tempPrice_df = 0
# get_symbols(ticker,start, end)
#
# tempPrice_df < - data.frame(tempPrice_df)
# tempPrice_df$Date < - rownames(tempPrice_df)
# rownames(tempPrice_df) < - NULL
# tempPrice_df < - tempPrice_df[order(tempPrice_df$Date, decreasing = FALSE), ]

# If the max date of the financial statement does not equal a date in the tempPrice_df, then subtract the Date by 1, then loop till TRUE
if x is True:
    pass
# if (Dates[x] == sort(tempPrice_df$Date)[1]){
# tempPrice_df = cbind(tempPrice_df[1, ], "Ticker"=ticker[i])
# colnames(tempPrice_df) = sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice_df = rbind(ClosePrice_df, tempPrice_df)
# check = True
else:
    pass
# Dates[x] < - as.character(as.Date(Dates[x]) - 1)

# It is possible that the company was not a publicly traded company during the date on the financial statment, so won't have matching stock price data. Once counter = 5 then stop the program
# if counter == 5:
# tempPrice_df = data.frame("Open"="NA", "High"="NA", "Low"="NA", "Close"="NA", "Volume"="NA", "Adjusted"="NA",
# "Date"=unique(temp_data$Date)[x], "Ticker" = ticker[i])
# ClosePrice_df = rbind(ClosePrice_df, tempPrice_df)
# check = TRUE

'''
The logic for this script is as follows. Subsetting the Qtrdata and data dataframes. Then because BalanceSheet and CashFlow statements are not supposed to have the trailing twelve months aggregated
these statements get the latest quarter(s) data if not equal to the latest annual data and are rbinded into 'test' data frame.
The Income Statement has the last four quarters summed aggregated if the latest quarter is not eqaual to the latest reported annual income statement and will be notes as "Yes" in ttm column
'''

# test < - data.frame()
# # Clean data to get ttm data
# for (i in 1:length(ticker)){
# temp_qtrdf < - Qtrdata[Qtrdata$Ticker == ticker[i], ]
# temp_df < - data[data$Ticker == ticker[i], ]
# financestats < - c("BalanceSheet")
# for (x in 1:length(financestats)){
#     temp < - temp_qtrdf[temp_qtrdf$FinancialStatement == financestats[x],]
# dates < - sort(as.character(unique(temp$Date)), decreasing = TRUE)[1:4]
# k < - 1
# while (dates[k] > max(temp_df$Date)){
# temp2 < - temp[temp$Date == dates[k], ]
# if (k == 1){
# test < - rbind(test, cbind(temp2, ttm="Quarterly Data"))
# } else {
# test < - rbind(test, cbind(temp2, ttm="Quarterly Data"))
# }
#
# k < - k + 1
# }
# if (k == 1 & x == 1){
# MaxDateBS < - temp_df[temp_df$FinancialStatement == "BalanceSheet", ]
# MaxDateBS < - max(MaxDateBS$Date)
# test < - rbind(test, cbind(temp_df[temp_df$Date == MaxDateBS & temp_df$FinancialStatement == "BalanceSheet", ], ttm="No"))
# test < - rbind(test, cbind(temp_df[temp_df$Date != MaxDateBS & temp_df$FinancialStatement == "BalanceSheet", ], ttm="No"))
# } else if (x == 1) {
# test < - rbind(test, cbind(temp_df[(temp_df$FinancialStatement == "BalanceSheet"), ], ttm="No"))
# }
# }
# financestats < - "IncomeStatement"
# temp < - temp_qtrdf[temp_qtrdf$FinancialStatement == financestats[1],]
# checkdate < - temp_df[temp_df$FinancialStatement == financestats[1],]
# checkdate < - max(as.character(checkdate$Date))
# dates < - sort(as.character(unique(temp$Date)), decreasing = TRUE)[1:4]
# k < - 1
# if (dates[k] > max(temp_df$Date)){
# maxDate < - dates[k]
# temp2 < - temp[temp$Date == dates[1],]
# temp3 < - temp[temp$Date == dates[2],]
# temp4 < - temp[temp$Date == dates[3],]
# temp5 < - temp[temp$Date == dates[4],]
# test6 < - cbind(rbind(temp2, temp3, temp4, temp5), ttm="Yes")
# test7 < - cbind(aggregate(Value
# ~ FinancialStatement + Metric + Ticker + ttm, test6, FUN = sum), "Date" = maxDate)
# test < - rbind(test, test7)
# test < - rbind(test, cbind(temp_df[temp_df$Date < max(as.character(
#     test7$Date)) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "No"))
# } else {
# test < - rbind(test, cbind(temp_df[temp_df$Date == max(
#     temp_df$Date) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "Yes"))
# test < - rbind(test, cbind(temp_df[temp_df$Date != max(
#     temp_df$Date) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "No"))
# }
#
# }
#
# data_finaldf < - rbind(test, cbind(data[data$FinancialStatement == "CashFlow",], ttm = "No"))
#
#
#
# # Create data frame to calculate the PE Valuation Model
# PE_df < - data.frame()
# for (i in 1:length(ticker)){
#
# # Filter to get needed data to calculate EPS
# temp_ttm_df2 < - data_finaldf[(data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker == ticker[i] & data_finaldf$ttm == "No"), ]
# temp_ttm_df < - data_finaldf[(data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "IncomeStatement" & data_finaldf$Metric == "Net Income" & data_finaldf$Date <= max(as.Date(as.character(temp_ttm_df2$Date)))), ]
#
# # Get the most current closing stock price and stock price for the previous years
# tempClosePrice < - ClosePrice_df[ClosePrice_df$Ticker == ticker[i], ]
# recentClosePrice < -
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE)
# recentClosePrice < - data.frame(recentClosePrice)
# recentClosePrice$Date < - rownames(recentClosePrice)
# row.names(recentClosePrice) < - NULL
# MostRecentClosePrice < - recentClosePrice[nrow(recentClosePrice), 4]
# MostRecentCloseDate < - recentClosePrice[nrow(recentClosePrice), ncol(recentClosePrice)]
#
# # Calculate EPS ttm for each of the years we have available
# EPS_ttm < - round(temp_ttm_df$Value / temp_ttm_df2$Value, digits = 2)
#
# # Calculate the PE ratio for each of the years we have avaailable
# PE_Ratio < - round(tempClosePrice$Close / EPS_ttm, digits = 2)
#
# # Create the PE data frame
# PE_df < - rbind(PE_df, cbind("Ticker" = ticker[i], "Date" = temp_ttm_df2$Date, "ClosePrice" = round(
#     tempClosePrice$Close, digits = 2), "NetIncome" = temp_ttm_df$Value,
#                                                                  "SharesOutstanding" = temp_ttm_df2$Value, "EPS" = EPS_ttm, "PE_Ratio" = PE_Ratio))
#
# PE_df < - rbind(PE_df, cbind("Ticker" = ticker[i], "Date" = MostRecentCloseDate, "ClosePrice" = round(
#     MostRecentClosePrice, digits=2), "NetIncome" = temp_ttm_df$Value[1],
#                                                                "SharesOutstanding" = temp_ttm_df2$Value[1], "EPS" =
# EPS_ttm[1], "PE_Ratio" = round(MostRecentClosePrice / EPS_ttm[1], digits=2)))
# }
# PE_df$Date < - as.Date(as.character(PE_df$Date))
# PE_df < - PE_df[order(PE_df$Ticker, PE_df$Date, decreasing = TRUE), ]
# PE_df$Ticker < - as.character(PE_df$Ticker)
# PE_df$ClosePrice < - as.numeric(as.character(PE_df$ClosePrice))
# PE_df$NetIncome < - as.numeric(as.character(PE_df$NetIncome))
# PE_df$SharesOutstanding < - as.numeric(as.character(PE_df$SharesOutstanding))
# PE_df$EPS < - as.numeric(as.character(PE_df$EPS))
# PE_df$PE_Ratio < - as.numeric(as.character(PE_df$PE_Ratio))
#
# # Plot the EPS growth, linear fit, and do not include the last EPS since that value is repeat from last calculated from annual financial statements
# TempPE_df < - PE_df[PE_df$Date != max(PE_df$Date), ]
# ggplot(TempPE_df, aes(x=Date, y=EPS, color=Ticker)) + geom_point() + stat_smooth(method="lm") + facet_grid(~ Ticker)
#
# # Now perform the PE valuation model
# PEValuation_df < - data.frame()
# for (i in 1:length(ticker)){
#
# # Get the median PE ratio for the past years
# MedianPE_df < - PE_df[PE_df$Ticker == ticker[i],]
# MedianPE < - median(MedianPE_df$PE_Ratio)
#
# # Get the company's most recent reported EPS (ttm)
# EPS < - PE_df[PE_df$Ticker == ticker[i],]$EPS[1]
#
# # Calculate EPS growth rate
# temp.df < - TempPE_df[TempPE_df$Ticker == ticker[i],]
# linearModel < - lm(EPS
# ~ Date, data = temp.df)
# OneYearValue < - as.vector(((as.numeric(temp.df$Date[1]) + 365) * coefficients(linearModel)[2]) +
#                     coefficients(linearModel)[1])
# PEGrowthRate < - round((OneYearValue / temp.df$EPS[1]) - 1, digits=3)
#
# # Get the close price of the stock
# tempPrice_df < - data.frame(
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE))
# colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice < - tempPrice_df$Close[nrow(tempPrice_df)]
#
# if (PEGrowthRate < 0 & ExpectedGrowthRate <= 0) {  # Apply the margin of safety on the growth rate
# PEConservative_GrowthRate < - PEGrowthRate * (1 + MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = PEGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                             "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                        "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                 "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
# } else if (ExpectedGrowthRate <= 0){
# PEConservative_GrowthRate < - PEGrowthRate * (1 - MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = PEGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                             "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                        "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                 "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
# } else {
# PEConservative_GrowthRate < - ExpectedGrowthRate * (1 - MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = ExpectedGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                                   "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                              "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                       "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
#
# }
#
# }
#
#
# ##Perform the DCF Valuation Model
# # Aggregate the data to get the free cash flow data
# FreeCashFlowAll_df < - data_finaldf[
#     (data_finaldf$Metric == "Capital Expenditures" | data_finaldf$Metric == "Cash from Operating Activities"),]
# FreeCashFlowAll_df < - FreeCashFlowAll_df[order(as.character(
#     FreeCashFlowAll_df$Ticker), FreeCashFlowAll_df$Date, decreasing = FALSE), ]
# FreeCashFlowAll_df < - aggregate(Value
# ~ FinancialStatement + Date + Ticker, FreeCashFlowAll_df, FUN = sum)
#
#
# # Loop to get the cash flow growth rate for each of the tickers, using the slope as growth rate
# DCF_finaldf < - data.frame()
# DCF_finaldf2 < - data.frame()
#
# # Create the final data frame for free cash flow valuation
# for (i in 1:length(ticker)){
# temp < - FreeCashFlowAll_df[FreeCashFlowAll_df$Ticker == ticker[i], ]
# temp < - temp[order(as.Date(temp$Date), decreasing = TRUE), ]
# temp$Date < - as.Date(temp$Date)
# tempvary < - temp$Value
# tempvarx < - temp$Date
# linearmodel < - lm(tempvary ~ tempvarx)
#
# # Calculate Cash Flows prediction using regression line, based on the date as sole independent variable. Formula is y=mx + b. Use prediction in one year to get growth rate from
# # value of most recent year to the predicted cash flow value one year from now
# Prediction_One_Year < - as.numeric(temp$Date[1] + 365) * coefficients(linearmodel)[[2]] + coefficients(linearmodel)[[1]]
# DCFGrowthRate < - round((Prediction_One_Year / temp$Value[1]) - 1, digits = 3)
#
#
# maxCashFlow < - temp[temp$Date == max(temp$Date), ]
#
# for (x in 1:DCF_YearsProjection){
# if (x == 1){  # When i is equal to 1 then do not include the growth decline rate
# tempYR1 < - maxCashFlow$Value[1] * (1 + (DCFGrowthRate * MarginSafety))
# tempPrice_df < - data.frame(
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE))
# colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice < - tempPrice_df$Close[nrow(tempPrice_df)]
# FCF < - maxCashFlow$Value[1]
# SharesOutstanding < - data_finaldf[data_finaldf$Date == maxCashFlow$Date[1] & data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker == ticker[i], ]$Value[1]
#
# Days < - 365
# if (DCFGrowthRate < 0 & ExpectedGrowthRate <= 0) {
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 + MarginSafety))), digits=2)
# } else if (ExpectedGrowthRate <= 0){
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 - MarginSafety))), digits=2)
# } else {
# DCFGrowthRate < - ExpectedGrowthRate
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 - MarginSafety))), digits=2)
# }
# NPV_ProjFCF < - round(ProjectedFCF / ((1 + DiscountRate) ^ x), digits=2)
#
# DCF_finaldf < - rbind(DCF_finaldf,
#                       cbind(temp, "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = c(
#     SharesOutstanding, "NA", "NA", "NA"),
#                                                                                                                                                                                                      "Formula" = "NA", "Predicted_FCF_Value" = "NA",
#                                                                                                                                                                                                                                                "NetPresentValue(PredictedValue)" = "NA", "Most_Current_StockPrice" = ClosePrice))
#
# DCF_finaldf < - rbind(DCF_finaldf, cbind("FinancialStatement" = "CashFlow", "Date" =as.character(as.Date(maxCashFlow$
# Date[1]) + Days), "Ticker" = ticker[i], "Value" = "NA",
#                                                   "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                      "Formula" = paste(
#     FCF, "*(1+(", DCFGrowthRate, "*(1-", MarginSafety, "))", sep=""),
#                                                                                                                                                                                                                                  "Predicted_FCF_Value" = ProjectedFCF, "NetPresentValue(PredictedValue)" = NPV_ProjFCF, "Most_Current_StockPrice" = ClosePrice))
#
# Days < - Days + 365
# } else {
#     FCF_temp < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i],]
# FCF < - FCF_temp[order(FCF_temp$Date, decreasing = TRUE), ]
# FCF < - as.numeric(as.character(FCF$Predicted_FCF_Value)[1])
# if (DCFGrowthRate < 0 & ExpectedGrowthRate <= 0) {
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 + MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
# } else if (ExpectedGrowthRate <= 0){
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 - MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
# } else {
# DCFGrowthRate < - ExpectedGrowthRate
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 - MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
#
# }
# NPV_ProjFCF < - round(ProjectedFCF / ((1 + DiscountRate) ^ x), digits=2)
#
# DCF_finaldf < - rbind(DCF_finaldf, cbind("FinancialStatement" = "CashFlow", "Date" =as.character(as.Date(maxCashFlow$
# Date[1]) + Days), "Ticker" = ticker[i], "Value" = "NA",
#                                                   "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                      "Formula" = paste(
#     FCF, "*(1+((", DCFGrowthRate, "*(1-", MarginSafety, "))*((1-", GrowthDeclineRate, ")^(", x, "-1))))", sep=""),
#                                                                                                                                                                                                                                  "Predicted_FCF_Value" = ProjectedFCF, "NetPresentValue(PredictedValue)" = NPV_ProjFCF, "Most_Current_StockPrice" = ClosePrice))
# Days < - Days + 365
#
# if (x == DCF_YearsProjection)
# {
# # Use the gordon growth model to calculate terminal value
# CF_FinalYear < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i],]
# CF_FinalYear < - CF_FinalYear[CF_FinalYear$Date == max(CF_FinalYear$Date), ]
# CF_FinalYear < - as.numeric(as.character(CF_FinalYear$Predicted_FCF_Value[1]))
#
# Terminal_Value < - round((CF_FinalYear * (1 + LongTermGrowthRate)) / (DiscountRate - LongTermGrowthRate), digits=2)
# NPV_Terminal_Value < - round(Terminal_Value / ((1 + .1) ^ x), digits=2)
#
# TotalNPV_FCF < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i] & DCF_finaldf$`NetPresentValue(PredictedValue)` != "NA",]
# TotalNPV_FCF < - sum(as.numeric(as.character(TotalNPV_FCF$`NetPresentValue(PredictedValue)`)))
#
# Cash_Equivalents < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$Metric == "Cash & Equivalents" & data_finaldf$Date == maxCashFlow$Date[1],]$Value[1]
# LongTermDebt < - (data_finaldf[data_finaldf
#     $Ticker == ticker[i] & data_finaldf$Metric == "Total Long Term Debt" & data_finaldf$Date == maxCashFlow$Date[1], ]$Value[1]) * -1
# Company_Value < - round(sum(NPV_Terminal_Value, TotalNPV_FCF, Cash_Equivalents, LongTermDebt, na.rm = TRUE), digits = 2)
#
# DCF_finaldf2 < - rbind(DCF_finaldf2, cbind("Ticker" = ticker[
#                                                           i], "Total_NPV_FCF" = TotalNPV_FCF, "Terminal_Value" = Terminal_Value, "NPV(Terminal_Value)" = NPV_Terminal_Value,
#                                                                                                                                                          "Cash & Cash Equivalents" = Cash_Equivalents, "Long_Term_Debt" = LongTermDebt, "Company_Value" = Company_Value, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                                                                                                 "DCF_Valuation" = round(
#     Company_Value / SharesOutstanding, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
#
# }
# }
# }
# }
#
# DCF_finaldf < - DCF_finaldf[order(DCF_finaldf$Ticker, DCF_finaldf$Date, decreasing = TRUE), ]
# row.names(DCF_finaldf$Date) < - NULL
#
# ggplot(DCF_finaldf, aes(x= as.Date(Date), y = as.numeric(Value), fill = Ticker)) + geom_bar()
#
# ##Miscellaneous metrics
#
# # Show cash and cash equivalents over time
# Cash_Equivalents_df < - data.frame()
# for (i in 1:length(ticker)){
# CashEquivalents_temp < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$Metric == "Cash & Equivalents", ][, 3:5]
# Cash_Equivalents_df < - rbind(Cash_Equivalents_df, CashEquivalents_temp)
#
# }
# Cash_Equivalents_df[, 1] < - as.character(Cash_Equivalents_df[, 1])
# Cash_Equivalents_df[, 2] < - as.numeric(as.character(Cash_Equivalents_df[, 2]))
# Cash_Equivalents_df[, 3] < - as.character(Cash_Equivalents_df[, 3])
# ggplot(Cash_Equivalents_df, aes(x=as.Date(Date), y = Value, fill = Ticker, label = Value)) +
#                                                                                            geom_bar(stat="identity",
#                                                                                                     width=100,
#                                                                                                     color="gray") + facet_grid(
#     ~ Ticker) + geom_text(vjust=-.25) +
#                                                                                            ggtitle(
#                                                                                                "Cash & Cash Equivalents") + labs(
#     x="Date", y="Cash & Cash Equivalents") +
#                                                                                            theme(
#                                                                                                plot.title = element_text(
#     hjust=0.5))
#
#
#
# # Show book value per share over time
# ShareHoldersEquity_df < - data.frame()
# for (i in 1:length(ticker)){
# SharesOutstanding < - data_finaldf[data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker == ticker[i], ]
# SharesOutstanding < - SharesOutstanding[order(SharesOutstanding$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets", ]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities", ]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# BookValue_Share < - round(ShareholdersEquity / SharesOutstanding$Value, digits = 3)
#
# ShareHoldersEquity_df < - rbind(ShareHoldersEquity_df, cbind("Ticker"=ticker[i], "Date"=SharesOutstanding$Date, "Total_Assets"=ShareholdersEquity_Assets$Value, "Total_Liabilities"=ShareholdersEquity_Liabilities$Value,
# "ShareHolders_Equity"=ShareholdersEquity, "BookValue_Share"=BookValue_Share))
# }
# ShareHoldersEquity_df[, 1] < - as.character(ShareHoldersEquity_df[, 1])
# ShareHoldersEquity_df[, 2] < - as.Date(as.character(ShareHoldersEquity_df[, 2]))
# ShareHoldersEquity_df[, 3] < - as.numeric(as.character(ShareHoldersEquity_df[, 3]))
# ShareHoldersEquity_df[, 4] < - as.numeric(as.character(ShareHoldersEquity_df[, 4]))
# ShareHoldersEquity_df[, 5] < - as.numeric(as.character(ShareHoldersEquity_df[, 5]))
# ShareHoldersEquity_df[, 6] < - as.numeric(as.character(ShareHoldersEquity_df[, 6]))
# ggplot(ShareHoldersEquity_df, aes(x=Date, y=BookValue_Share, fill=Ticker, label=BookValue_Share)) +
# geom_bar(stat = "identity", width = 100, color = "gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Book Value per Share") + labs(x="Date", y="Book Vaue per Share") +
# theme(plot.title = element_text(hjust = 0.5))
#
#
#
# # Show net margin over time
# NetMargin_df < - data.frame()
# for (i in 1:length(ticker)){
#     Revenue_df < - data_finaldf[data_finaldf$Metric == "Total Revenue" & data_finaldf$Ticker == ticker[i],]
# Revenue_df < - Revenue_df[order(Revenue_df$Date, decreasing = TRUE), ]
#
# NetIncome_df < - data_finaldf[data_finaldf$Metric == "Net Income" & data_finaldf$Ticker == ticker[i],]
# NetIncome_df < - NetIncome_df[order(NetIncome_df$Date, decreasing = TRUE), ]
#
# NetMargin < - round(NetIncome_df$Value / Revenue_df$Value, digits = 3)
#
# NetMargin_df < - rbind(NetMargin_df, cbind("Ticker" = ticker[i], "Date" = Revenue_df$Date, "Revenue" = Revenue_df$Value,
#                                                                                                                   "Net_Income" = NetIncome_df$Value, "NetMargin" = NetMargin))
# }
# NetMargin_df[, 1] < - as.character(NetMargin_df[, 1])
# NetMargin_df[, 2] < - as.Date(as.character(NetMargin_df[, 2]))
# NetMargin_df[, 3] < - as.numeric(as.character(NetMargin_df[, 3]))
# NetMargin_df[, 4] < - as.numeric(as.character(NetMargin_df[, 4]))
# NetMargin_df[, 5] < - as.numeric(as.character(NetMargin_df[, 5]))
# ggplot(NetMargin_df, aes(x=Date, y=NetMargin, fill=Ticker, label=NetMargin)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Net Margin") + labs(x="Date", y="Net Margin") +
# theme(plot.title = element_text(hjust=0.5))
#
#
# # Show return on equity over time
# ReturnEquity_df < - data.frame()
# for (i in 1:length(ticker)){
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets" & data_finaldf$ttm != "Quarterly Data", ]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities" & data_finaldf$ttm != "Quarterly Data", ]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# NetIncome_df < - data_finaldf[data_finaldf$Metric == "Net Income" & data_finaldf$Ticker == ticker[i], ]
# NetIncome_df < - NetIncome_df[NetIncome_df$Date <= max(ShareholdersEquity_Assets$Date), ]
# NetIncome_df < - NetIncome_df[order(NetIncome_df$Date, decreasing = TRUE), ]
#
# ReturnEquity < - round(NetIncome_df$Value / ShareholdersEquity, digits = 3)
#
# ReturnEquity_df < - rbind(ReturnEquity_df, cbind("Ticker"=ticker[i], "Date"=ShareholdersEquity_Assets$Date, "Net_Income"=NetIncome_df$Value, "Total_Assets"=ShareholdersEquity_Assets$Value,
# "Total_Liabilities"=ShareholdersEquity_Liabilities$Value, "ShareHolders_Equity"=ShareholdersEquity, "ReturnEquity"=ReturnEquity))
#
# }
# ReturnEquity_df[, 1] < - as.character(ReturnEquity_df[, 1])
# ReturnEquity_df[, 2] < - as.Date(as.character(ReturnEquity_df[, 2]))
# ReturnEquity_df[, 3] < - as.numeric(as.character(ReturnEquity_df[, 3]))
# ReturnEquity_df[, 4] < - as.numeric(as.character(ReturnEquity_df[, 4]))
# ReturnEquity_df[, 5] < - as.numeric(as.character(ReturnEquity_df[, 5]))
# ReturnEquity_df[, 6] < - as.numeric(as.character(ReturnEquity_df[, 6]))
# ReturnEquity_df[, 7] < - as.numeric(as.character(ReturnEquity_df[, 7]))
# ggplot(ReturnEquity_df, aes(x=Date, y=ReturnEquity, fill=Ticker, label=ReturnEquity)) +
# geom_bar(stat = "identity", width = 100, color = "gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Return on Equity") + labs(x="Date", y="Return on Equity") +
# theme(plot.title = element_text(hjust = 0.5, size = 25))
#
#
#
#
# # Show long term debt to equity over time
# DebtEquity_df < - data.frame()
# for (i in 1: length(ticker)){
#     LongTermDebt_df < - data_finaldf[data_finaldf$Metric == "Total Long Term Debt" & data_finaldf$Ticker == ticker[i],]
# LongTermDebt_df < - LongTermDebt_df[order(LongTermDebt_df$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets",]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities",]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[
#     order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# DebtEquity < - round(LongTermDebt_df$Value / ShareholdersEquity, digits = 3)
#
# DebtEquity_df < - rbind(DebtEquity_df, cbind("Ticker" = ticker[
#                                                             i], "Date" = ShareholdersEquity_Assets$Date, "LongTermDebt" = LongTermDebt_df$Value, "Total_Assets" = ShareholdersEquity_Assets$Value,
#                                                                                                                                                                                             "Total_Liabilities" = ShareholdersEquity_Liabilities$Value, "ShareHolders_Equity" = ShareholdersEquity, "DebtToEquity" = DebtEquity))
#
# }
# DebtEquity_df[, 1] < - as.character(DebtEquity_df[, 1])
# DebtEquity_df[, 2] < - as.Date(as.character(DebtEquity_df[, 2]))
# DebtEquity_df[, 3] < - as.numeric(as.character(DebtEquity_df[, 3]))
# DebtEquity_df[, 4] < - as.numeric(as.character(DebtEquity_df[, 4]))
# DebtEquity_df[, 5] < - as.numeric(as.character(DebtEquity_df[, 5]))
# DebtEquity_df[, 6] < - as.numeric(as.character(DebtEquity_df[, 6]))
# DebtEquity_df[, 7] < - as.numeric(as.character(DebtEquity_df[, 7]))
# ggplot(DebtEquity_df, aes(x=Date, y=DebtToEquity, fill=Ticker, label=DebtToEquity)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Long Term Debt to Equity Ratio") + labs(x="Date", y="Long Term Debt to Equity") +
# theme(plot.title = element_text(hjust=0.5))
#
#
#
# # Give the page a title
# # "Fundamental Stock Analysis"
#
# # Generate a row with a sidebar
#
# # Define the sidebar layout
# textInput(inputId="ticker", label="Stock Ticker(s):", value=paste(c("MSFT", "GOOG", "AMZN"), collapse=",")),
# "Enter Stock Tickers, separated by commas, no spaces. Recommended to not input more than four stock tickers. Please be patient as the data takes a little while to load."
#
# sliderInput(inputId="ExpectedGrowthRate", label="Expected Growth Rate:", min=-.01, max=.30, value=-.01, step=.01),
# "When the expected growth rate is negative, the growth rate is equal to the slope of the regression line (Date used as sole independent variable"
#
# sliderInput(inputId="MarginSafety", label="Margin of Safety", min=0, max=.30, value=.10, step=.01),
# "The margin of safety is applied to the expected growth rate, to come up with a conservative growth rate estimate."
#
# sliderInput(inputId="GrowthDeclineRate", label="Growth Decline Rate:", min=0, max=.15, value=.05, step=.01),
# "Growth decline rate is applied to the conservative growth rate one year after first year projections. This is because it is hard to keep consistent high growth rates in the long run."
#
# sliderInput(inputId="DiscountRate", label="Discount Rate:", min=0, max=.20, value=.09, step=.01),
# "Discount rate initially set to .09 because 9% rate of return is the historic long term growth of the stock market."
#
# sliderInput(inputId="DCF_YearsProjection", label="DCF Valuation Model. Number of years in future to project:", min=5, max=10, value=5, step=1),
# "Generally you would project a company's cash flows five to ten years in the future."
#
# sliderInput(inputId="LongTermGrowthRate", label="Long Term Cash Flow Growth Rate:", min=0.01, max=.05, value=.03, step=.01),\
# "The long term cash flow growth rate in the US economy is around three percent.",
#
# submitButton(text="Analyze")
#
# # Create a spot for the barplot
# tabPanel("Discounted Cash Flow Valuation Model",
# tabPanel("Analysis"
# ,p("Due to the amount of data being loaded and read, this app may take a couple seconds to load for each tab..."),
#
# "DCF_Model.plot"
# p("The DCF Model projects future cash flows and discounts them back to the present value; this is a valuation method that estimates the intrinsic value of an investment opportunity."),
#
# "DCF_Model.plot2"
# p("Generally recommended to look for a company with stable or increasing cash flows over time. The free cash flows of a company are hard to maintain at a high growth rate, so each year, the conservative growth rate will decline by the growth decline rate. Free cash flow is used for paying debts, dividends, buybacks, or investing in the future growth of a company.")),
#
# tabPanel("Data/Calculations",
#
# h2("DCF Valuation Table"),
# dataTableOutput("DCF_Model.table2"),
# h2("Free Cash Flows Projection and Values Table"),
# dataTableOutput("DCF_Model.table")
#
# tabPanel("Price Earnings Multiple Valuation Model",
# tabPanel("Analysis",
# plotOutput("PE_Model.plot"),
# p("In this method, a five-year price target is determined based on historical P/E valuation."),
# plotOutput("PE_Model.plot2"),
# p("The Earnings per share is the profit that a company makes per share of stock. A growing EPS is better than it decreasing or staying stable. Calculated by dividing 'Net Income / Shares Outstanding'.")),
# tabPanel("Data/Calculations",
# h2("PE Valuation Table"),
# dataTableOutput("PE_Model.table"),
#
# h2("EPS Table"),
# dataTableOutput("PE_Model.table2")
#
# # "Fundamental Analysis"
#
# "Analysis",
# # "Cash_Equivalents.plot"
# p("Generally recommended to look for Cash and Equivalents to increase over time. Reported on the balance sheet. An increasing value means that there is more cash reserves over time. Even if this metric is decreasing over time, the company can just be investing the reserve money to improve the business."),
#
#
# # "Book_Value.plot"
# p("Generally recommended to look for book value to increase over time. This shows how much money, you would receive for your shares of stock if the company liquidates, selling all of its assets after paying off its debts. You want to look for companies with increasing book value per share because they are companies that are creating value. To calculate: 'Shareholders Equity / Shares Outstanding'."),
#
# # "Net_Margin.plot"
# p("Generally recommended to look for net margin to increase over time. Net margin is what percent of sales is profit. This figure differs greatly from industry to industry. If a company is able to sustain high profit margins, then the company may have a strong brand name or patented products that competitors can't compete with. The higher the net margin, the better. To calculate 'Net Income / Revenue'."),
#
# # "Return_Equity.plot"
# p("Generally recommended that return on equity is consistently high. Return on equity tells us how efficiently a company uses its assets to generate earnings. The higher the return on equity, the better. To calculate: 'Net Income / Shareholders Equity"),
#
# # "Debt_Equity.plot"
# p("Generally recommended to look for debt to equity that has been consistently low or decreasing. Long term debt to equity ratio indicates how much debt a company in relation to its shareholder's equity. High debt levels are a huge warning sign as it relies on debt to finance its growth. If a company has an increasing debt to equity ratio, then the investment may become risky because the company cannot meet its debt obligations. To calculate: 'Long-Term Debt / Shareholders Equity'")),
# tabPanel("Data/Calculations",
#
# # "Cash Equivalents Table"
# dataTableOutput("Cash_Equivalents.table"),
#
# # "Book Value per Share Table"
# dataTableOutput("Book_Value.table"),
#
# # "Net/Profit Margin Table"
# dataTableOutput("Net_Margin.table"),
#
# # "Return on Equity Table"
# dataTableOutput("Return_Equity.table"),
#
# # "Long Term Debt to Equity Table"
# dataTableOutput("Debt_Equity.table")
#
# # "Financial Statements",
# dataTableOutput("FinanceData.table")
#
#
# ##Get the annual financial statement data
# data < - function(ticker)
# {
#
#     ##Get the financial statement data of the tickers for the past four years
#     data < - data.frame()
#     for (i in 1:length(ticker)){
#
#     # Get the stock ticker information
#     temp_data < -
# try(getFinancials(ticker[i], type=c('BS', 'IS', 'CF'), period=c('A'), auto.assign = FALSE), silent=TRUE)
#
# # Create temporary data frames for each of the financial statments
# temp_dataBS < - data.frame(temp_data$BS$A, FinancialStatement = "BalanceSheet")
# temp_dataBS$Metric < - rownames(temp_dataBS)
# temp_dataIS < - data.frame(temp_data$IS$A, FinancialStatement = "IncomeStatement")
# temp_dataIS$Metric < - rownames(temp_dataIS)
# temp_dataCF < - data.frame(temp_data$CF$A, FinancialStatement = "CashFlow")
# temp_dataCF$Metric < - rownames(temp_dataCF)
# temp_data < - rbind(melt(temp_dataBS, id=c("Metric", "FinancialStatement")),
#                     melt(temp_dataIS, id=c("Metric", "FinancialStatement")),
#                     melt(temp_dataCF, id=c("Metric", "FinancialStatement")))
#
# # Rbind the data to append ticker information
# data < - rbind(data, cbind(temp_data, "Ticker" = ticker[i]))
# }
#
#
#
# # Rename some column variables
# colnames(data)[3] < - "Date"
# colnames(data)[4] < - "Value"
#
# ##Clean out the Date column
# data$Date < - gsub("\\.", "-", data$Date)
# data$Date < - sub("[A-Z]", "", data$Date)
#
# # Return the data frame
# data
# }
#
#
# ##Get the quarterly financial statement data
# Qtrdata < - function(ticker)
# {
#
#     ##Get the financial statement data of the tickers for the past four quarters
#     Qtrdata < - data.frame()
#     for (i in 1:length(ticker)){
#
# # Get the stock ticker information
# temp_data < -
# try(getFinancials(ticker[i], type=c('BS', 'IS', 'CF'), period=c('Q'), auto.assign = FALSE), silent=TRUE)
#
# # Create temporary data frames for each of the financial statments
# temp_dataBS < - data.frame(temp_data$BS$Q, FinancialStatement = "BalanceSheet")
# temp_dataBS$Metric < - rownames(temp_dataBS)
# temp_dataIS < - data.frame(temp_data$IS$Q, FinancialStatement = "IncomeStatement")
# temp_dataIS$Metric < - rownames(temp_dataIS)
# temp_dataCF < - data.frame(temp_data$CF$Q, FinancialStatement = "CashFlow")
# temp_dataCF$Metric < - rownames(temp_dataCF)
#
# # Melt the data to reshape the date column variables into a value under a single variable
# rownames(temp_dataBS) < - NULL
# rownames(temp_dataIS) < - NULL
# rownames(temp_dataCF) < - NULL
# temp_dataBS < - melt(temp_dataBS, id=c("Metric", "FinancialStatement"))
# temp_dataIS < - melt(temp_dataIS, id=c("Metric", "FinancialStatement"))
# temp_dataCF < - melt(temp_dataCF, id=c("Metric", "FinancialStatement"))
# temp_data < - rbind(temp_dataBS, temp_dataIS, temp_dataCF)
#
# # Rbind the data to append ticker information
# Qtrdata < - rbind(Qtrdata, cbind(temp_data, "Ticker" = ticker[i]))
# }
#
# # Rename some column variables
# colnames(Qtrdata)[3] < - "Date"
# colnames(Qtrdata)[4] < - "Value"
#
# ##Clean out the Date column
# Qtrdata$Date < - gsub("\\.", "-", Qtrdata$Date)
# Qtrdata$Date < - sub("[A-Z]", "", Qtrdata$Date)
#
# # Return the Quarterly data
# Qtrdata
# }
#
#
# ##Consolidated data of annual/quarterly financial statement data
# data_finaldf < - function(ticker)
# {
#
#     # Load financial data from other functions
#     data < - data(ticker)
# Qtrdata < - Qtrdata(ticker)
#
# # The logic for this script is as follows. Subsetting the Qtrdata and data dataframes. Then because BalanceSheet and CashFlow statements are not supposed to have the trailing twelve months aggregated
# # these statements get the latest quarter(s) data if not equal to the latest annual data and are rbinded into 'test' data frame.
# # The Income Statement has the last four quarters summed aggregated if the latest quarter is not eqaual to the latest reported annual income statement and will be notes as "Yes" in ttm column
# test < - data.frame()
# # Clean data to get ttm data
# for (i in 1:length(ticker)){
# temp_qtrdf < - Qtrdata[Qtrdata$Ticker == ticker[i],]
# temp_df < - data[data$Ticker == ticker[i],]
# financestats < - c("BalanceSheet")
# for (x in 1:length(financestats)){
# temp < - temp_qtrdf[temp_qtrdf$FinancialStatement == financestats[x], ]
# dates < - sort(as.character(unique(temp$Date)), decreasing = TRUE)[1:4]
# k < - 1
# while (dates[k] > max(temp_df$Date)){
# temp2 < - temp[temp$Date == dates[k], ]
# if (k == 1){
# test < - rbind(test, cbind(temp2, ttm="Quarterly Data"))
# } else {
# test < - rbind(test, cbind(temp2, ttm="Quarterly Data"))
# }
#
# k < - k + 1
# }
# if (k == 1 & x == 1){
# MaxDateBS < - temp_df[temp_df$FinancialStatement == "BalanceSheet", ]
# MaxDateBS < - max(MaxDateBS$Date)
# test < - rbind(test, cbind(temp_df[temp_df$Date == MaxDateBS & temp_df$FinancialStatement == "BalanceSheet", ], ttm="No"))
# test < - rbind(test, cbind(temp_df[temp_df$Date != MaxDateBS & temp_df$FinancialStatement == "BalanceSheet", ], ttm="No"))
# } else if (x == 1) {
# test < - rbind(test, cbind(temp_df[(temp_df$FinancialStatement == "BalanceSheet"), ], ttm="No"))
# }
# }
# financestats < - "IncomeStatement"
# temp < - temp_qtrdf[temp_qtrdf$FinancialStatement == financestats[1],]
# checkdate < - temp_df[temp_df$FinancialStatement == financestats[1],]
# checkdate < - max(as.character(checkdate$Date))
# dates < - sort(as.character(unique(temp$Date)), decreasing = TRUE)[1:4]
# k < - 1
# if (dates[k] > max(temp_df$Date)){
# maxDate < - dates[k]
# temp2 < - temp[temp$Date == dates[1],]
# temp3 < - temp[temp$Date == dates[2],]
# temp4 < - temp[temp$Date == dates[3],]
# temp5 < - temp[temp$Date == dates[4],]
# test6 < - cbind(rbind(temp2, temp3, temp4, temp5), ttm="Yes")
# test7 < - cbind(aggregate(Value
# ~ FinancialStatement + Metric + Ticker + ttm, test6, FUN = sum), "Date" = maxDate)
# test < - rbind(test, test7)
# test < - rbind(test, cbind(temp_df[temp_df$Date < max(as.character(
#     test7$Date)) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "No"))
# } else {
# test < - rbind(test, cbind(temp_df[temp_df$Date == max(
#     temp_df$Date) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "Yes"))
# test < - rbind(test, cbind(temp_df[temp_df$Date != max(
#     temp_df$Date) & temp_df$FinancialStatement == "IncomeStatement",], ttm = "No"))
# }
#
# }
#
#
# ##Return the consolidated dataset
# data_finaldf < - rbind(test, cbind(data[data$FinancialStatement == "CashFlow",], ttm = "No"))
# data_finaldf
#
# }
#
#
# ##Function for DCF Valuation Analysis
# DCF_Valuation < - function(Get, ticker, ExpectedGrowthRate, MarginSafety, GrowthDeclineRate,
#                            DiscountRate, DCF_YearsProjection, LongTermGrowthRate)
# {
#     ticker < - as.vector(strsplit(ticker, ",")[[1]])
# # Grab data from previous function
# data_finaldf < - data_finaldf(ticker)
#
# # Aggregate the data to get the free cash flow data
# FreeCashFlowAll_df < - data_finaldf[
#     (data_finaldf$Metric == "Capital Expenditures" | data_finaldf$Metric == "Cash from Operating Activities"),]
# FreeCashFlowAll_df < - FreeCashFlowAll_df[order(as.character(
#     FreeCashFlowAll_df$Ticker), FreeCashFlowAll_df$Date, decreasing = FALSE), ]
# FreeCashFlowAll_df < - aggregate(Value
# ~ FinancialStatement + Date + Ticker, FreeCashFlowAll_df, FUN = sum)
#
#
# # Loop to get the cash flow growth rate for each of the tickers, using the slope as growth rate
# DCF_finaldf < - data.frame()
# DCF_finaldf2 < - data.frame()
#
# # Create the final data frame for free cash flow valuation
# for (i in 1:length(ticker)){
# temp < - FreeCashFlowAll_df[FreeCashFlowAll_df$Ticker == ticker[i], ]
# temp < - temp[order(as.Date(temp$Date), decreasing = TRUE), ]
# temp$Date < - as.Date(temp$Date)
# tempvary < - temp$Value
# tempvarx < - temp$Date
# linearmodel < - lm(tempvary ~ tempvarx)
#
# # Calculate Cash Flows prediction using regression line, based on the date as sole independent variable. Formula is y=mx + b. Use prediction in one year to get growth rate from
# # value of most recent year to the predicted cash flow value one year from now
# Prediction_One_Year < - as.numeric(temp$Date[1] + 365) * coefficients(linearmodel)[[2]] + coefficients(linearmodel)[[1]]
# Prediction_current_Year < - as.numeric(temp$Date[1]) * coefficients(linearmodel)[[2]] + coefficients(linearmodel)[[1]]
# DCFGrowthRate < - round((Prediction_One_Year / Prediction_current_Year) - 1, digits = 3)
#
#
# maxCashFlow < - temp[temp$Date == max(temp$Date), ]
#
# for (x in 1:DCF_YearsProjection){
# if (x == 1){  # When i is equal to 1 then do not include the growth decline rate
# tempYR1 < - maxCashFlow$Value[1] * (1 + (DCFGrowthRate * MarginSafety))
# tempPrice_df < - data.frame(
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE))
# colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice < - tempPrice_df$Close[nrow(tempPrice_df)]
# FCF < - maxCashFlow$Value[1]
# SharesOutstanding < - data_finaldf[data_finaldf$Date == maxCashFlow$Date[1] & data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker == ticker[i], ]$Value[1]
#
# Days < - 365
# if (DCFGrowthRate < 0 & ExpectedGrowthRate <= 0) {
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 + MarginSafety))), digits=2)
# } else if (ExpectedGrowthRate <= 0){
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 - MarginSafety))), digits=2)
# } else {
# DCFGrowthRate < - ExpectedGrowthRate
# ProjectedFCF < - round(FCF * (1 + (DCFGrowthRate * (1 - MarginSafety))), digits=2)
# }
# NPV_ProjFCF < - round(ProjectedFCF / ((1 + DiscountRate) ^ x), digits=2)
#
# DCF_finaldf < - rbind(DCF_finaldf,
#                       cbind(temp, "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = c(
#     SharesOutstanding, "NA", "NA", "NA"),
#                                                                                                                                                                                                      "Formula" = "NA", "Predicted_FCF_Value" = "NA",
#                                                                                                                                                                                                                                                "NetPresentValue(PredictedValue)" = "NA", "Most_Current_StockPrice" = ClosePrice))
#
# DCF_finaldf < - rbind(DCF_finaldf, cbind("FinancialStatement" = "CashFlow", "Date" =as.character(as.Date(maxCashFlow$
# Date[1]) + Days), "Ticker" = ticker[i], "Value" = "NA",
#                                                   "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                      "Formula" = paste(
#     FCF, "*(1+(", DCFGrowthRate, "*(1-", MarginSafety, "))", sep=""),
#                                                                                                                                                                                                                                  "Predicted_FCF_Value" = ProjectedFCF, "NetPresentValue(PredictedValue)" = NPV_ProjFCF, "Most_Current_StockPrice" = ClosePrice))
#
# Days < - Days + 365
# } else {
#     FCF_temp < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i],]
# FCF < - FCF_temp[order(FCF_temp$Date, decreasing = TRUE), ]
# FCF < - as.numeric(as.character(FCF$Predicted_FCF_Value)[1])
# if (DCFGrowthRate < 0 & ExpectedGrowthRate <= 0) {
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 + MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
# } else if (ExpectedGrowthRate <= 0){
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 - MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
# } else {
# DCFGrowthRate < - ExpectedGrowthRate
# ProjectedFCF < - round(FCF * (1 + ((DCFGrowthRate * (1 - MarginSafety)) * ((1 - GrowthDeclineRate) ^ (x - 1)))),
#                        digits=2)
#
# }
# NPV_ProjFCF < - round(ProjectedFCF / ((1 + DiscountRate) ^ x), digits=2)
#
# DCF_finaldf < - rbind(DCF_finaldf, cbind("FinancialStatement" = "CashFlow", "Date" =as.character(as.Date(maxCashFlow$
# Date[1]) + Days), "Ticker" = ticker[i], "Value" = "NA",
#                                                   "ExpectedGrowthRate..CF_Slope" = DCFGrowthRate, "Margin_Safety" = MarginSafety,
#                                                                                                                     "GrowthDecline_Rate" = GrowthDeclineRate, "Discount_Rate" = DiscountRate, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                      "Formula" = paste(
#     FCF, "*(1+((", DCFGrowthRate, "*(1-", MarginSafety, "))*((1-", GrowthDeclineRate, ")^(", x, "-1))))", sep=""),
#                                                                                                                                                                                                                                  "Predicted_FCF_Value" = ProjectedFCF, "NetPresentValue(PredictedValue)" = NPV_ProjFCF, "Most_Current_StockPrice" = ClosePrice))
# Days < - Days + 365
#
# if (x == DCF_YearsProjection)
# {
# # Use the gordon growth model to calculate terminal value
# CF_FinalYear < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i],]
# CF_FinalYear < - CF_FinalYear[CF_FinalYear$Date == max(CF_FinalYear$Date), ]
# CF_FinalYear < - as.numeric(as.character(CF_FinalYear$Predicted_FCF_Value[1]))
#
# Terminal_Value < - round((CF_FinalYear * (1 + LongTermGrowthRate)) / (DiscountRate - LongTermGrowthRate), digits=2)
# NPV_Terminal_Value < - round(Terminal_Value / ((1 + .1) ^ x), digits=2)
#
# TotalNPV_FCF < - DCF_finaldf[DCF_finaldf$Ticker == ticker[i] & DCF_finaldf$`NetPresentValue(PredictedValue)` != "NA",]
# TotalNPV_FCF < - sum(as.numeric(as.character(TotalNPV_FCF$`NetPresentValue(PredictedValue)`)))
#
# Cash_Equivalents < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$Metric == "Cash & Equivalents" & data_finaldf$Date == maxCashFlow$Date[1],]$Value[1]
# LongTermDebt < - (data_finaldf[data_finaldf
#     $Ticker == ticker[i] & data_finaldf$Metric == "Total Long Term Debt" & data_finaldf$Date == maxCashFlow$Date[1], ]$Value[1]) * -1
# Company_Value < - round(sum(NPV_Terminal_Value, TotalNPV_FCF, Cash_Equivalents, LongTermDebt, na.rm = TRUE), digits = 2)
#
# DCF_finaldf2 < - rbind(DCF_finaldf2, cbind("Ticker" = ticker[
#                                                           i], "Total_NPV_FCF" = TotalNPV_FCF, "Terminal_Value" = Terminal_Value, "NPV(Terminal_Value)" = NPV_Terminal_Value,
#                                                                                                                                                          "Cash & Cash Equivalents" = Cash_Equivalents, "Long_Term_Debt" = LongTermDebt, "Company_Value" = Company_Value, "Shares_Outstanding" = SharesOutstanding,
#                                                                                                                                                                                                                                                                                                 "DCF_Valuation" = round(
#     Company_Value / SharesOutstanding, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
#
# }
# }
# }
# }
#
# DCF_finaldf < - DCF_finaldf[order(DCF_finaldf$Ticker, DCF_finaldf$Date, decreasing = TRUE), ]
# row.names(DCF_finaldf$Date) < - NULL
#
# # Conditional Statement for the return function
# if (Get == "Plot_1")
# {
#     # This plot will be on the Analysis tab, barplot to compare the DCF_Valuation and the stock price
#
#     temp_df < - data.frame(cbind("Ticker" =as.character(DCF_finaldf2$Ticker), "DCF_Valuation" =as.numeric(as.character(
#     DCF_finaldf2$DCF_Valuation)),
# "Most_Recent_Stock_Price" =as.numeric(as.character(DCF_finaldf2$Most_Current_Stock_Price))))
# temp_df < - melt(temp_df, id="Ticker")
#
# colnames(temp_df) < - c("Ticker", "Valuation Type", "Price")
# temp_df[, 1] < - as.character(temp_df[, 1])
# temp_df[, 2] < - as.character(temp_df[, 2])
# temp_df[, 3] < - as.numeric(as.character(temp_df[, 3]))
#
# ggplot(temp_df, aes(x=`Valuation
# Type
# `, y = Price, fill = `Valuation
# Type
# `, label = Price)) +
#                    geom_bar(stat="identity", color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
#                    ggtitle("Discounted Cash Flow Valuation") + labs(x="Valuation Type", y="Value ($)") +
#                    theme(plot.title = element_text(hjust=0.5), plot.margin = unit(c(.01, .01, .01, .01), "cm"))
#
# } else if (Get == "Plot_2") {
# # This plot will be on the Analysis tab, line plot to show the progression of cash flows
#
# temp_df < - data.frame(cbind("Date"=as.character((DCF_finaldf$Date)), "Ticker"=as.character(DCF_finaldf$Ticker), "FCF"=as.numeric(as.character(DCF_finaldf$Value)),
# "Predicted_FCF"=as.numeric(as.character(DCF_finaldf$Predicted_FCF_Value)),
# "NPV_Predicted_FCF"=as.numeric(as.character(DCF_finaldf$`NetPresentValue(PredictedValue)`))))
# temp_df < - melt(temp_df, id=c("Ticker", "Date"))
# temp_df[, 1] < - as.character(temp_df[, 1])
# temp_df[, 2] < - as.Date(as.character(temp_df[, 2]))
# temp_df[, 3] < - as.character(temp_df[, 3])
# temp_df[, 4] < - as.numeric(as.character(temp_df[, 4]))
#
# ggplot(temp_df, aes(x = Date, y = value, color = variable, label = round(value, digits = 0))) + geom_point(size=1.8) + geom_line(size=1.3) +
# facet_grid(~ Ticker) + geom_text(vjust=-1.4, size=3) + ggtitle("Free Cash Flow") +
# labs(x="Date", y="Free Cash Flow ($)") + theme(plot.title = element_text(hjust = 0.5, size = 25))
#
# } else if (Get == "Table_1") {
# # This table will be on the analysis tab, to show the free cash flows over the years and the calculations
# DCF_finaldf
# } else if (Get == "Table_2") {
# # This table will be on the analysis tab, to show/perform the DCF Valuation model and compare it to the most recent stock price
# DCF_finaldf2
# }
# }
#
#
# ##Function for the PE Valuation Analysis
# PE_Valuation < - function(Get, ticker, ExpectedGrowthRate, MarginSafety, DiscountRate){
# ticker < - as.vector(strsplit(ticker, ",")[[1]])
# # Grab data from previous function
# data_finaldf < - data_finaldf(ticker)
# data < - data(ticker)
#
# ##PE Valuation Data Cleansing for annual data
# ClosePrice_df < - data.frame()
# for (i in 1:length(ticker)){
#
#     # Get the unique dates for the stock ticker in the financial statements
#     temp_data < - data[data$Ticker == ticker[i],]
# temp_data < - temp_data[order(temp_data$Date, decreasing = TRUE), ]
# Dates < - unique(temp_data$Date)
#
# # Loop to get data for all unique dates in the financial statments
# for (x in 1:length(Dates)){
#
# # Check if the date in financial statments is found in the tempPrice_df
# check < - FALSE
# counter = 0
# while (check == FALSE){
#
# counter < - counter + 1
#
# # Get the ticker's stock price and append date column
# tempPrice_df < -
# try(getSymbols(ticker[i], from =Dates[x], auto.assign = FALSE, src='google'), silent = TRUE)
# tempPrice_df < - data.frame(tempPrice_df)
# tempPrice_df$Date < - rownames(tempPrice_df)
# rownames(tempPrice_df) < - NULL
# tempPrice_df < - tempPrice_df[order(tempPrice_df$Date, decreasing = FALSE), ]
#
# # If the max date of the financial statement does not equal a date in the tempPrice_df, then subtract the Date by 1, then loop till TRUE
# if (Dates[x] == sort(tempPrice_df$Date)[1]){
# tempPrice_df < - cbind(tempPrice_df[1, ], "Ticker"=ticker[i])
# colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice_df < - rbind(ClosePrice_df, tempPrice_df)
# check < - TRUE
# }
#
# else {
# Dates[x] < - as.character(as.Date(Dates[x]) - 1)
#
# # It is possible that the company was not a publicly traded company during the date on the financial statment, so won't have matching stock price data. Once counter = 5 then stop the program
# if (counter == 5){
# tempPrice_df < - data.frame("Open"="NA", "High"="NA", "Low"="NA", "Close"="NA", "Volume"="NA", "Adjusted"="NA",
# "Date"=unique(temp_data$Date)[x], "Ticker"=ticker[i])
# ClosePrice_df < - rbind(ClosePrice_df, tempPrice_df)
# check < - TRUE
# }
# }
# }
# }
# }
#
# # Create data frame to calculate the PE Valuation Model
# PE_df < - data.frame()
# for (i in 1:length(ticker)){
#
# # Filter to get needed data to calculate EPS
# temp_ttm_df2 < - data_finaldf[(data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker == ticker[i] & data_finaldf$ttm == "No"), ]
# temp_ttm_df < - data_finaldf[(data_finaldf$Ticker == ticker[i] & data_finaldf$FinancialStatement == "IncomeStatement" & data_finaldf$Metric == "Net Income" & data_finaldf$Date <= max(as.Date(as.character(temp_ttm_df2$Date)))), ]
#
# # Get the most current closing stock price and stock price for the previous years
# tempClosePrice < - ClosePrice_df[ClosePrice_df$Ticker == ticker[i], ]
# recentClosePrice < -
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE)
# recentClosePrice < - data.frame(recentClosePrice)
# recentClosePrice$Date < - rownames(recentClosePrice)
# row.names(recentClosePrice) < - NULL
# MostRecentClosePrice < - recentClosePrice[nrow(recentClosePrice), 4]
# MostRecentCloseDate < - recentClosePrice[nrow(recentClosePrice), ncol(recentClosePrice)]
#
# # Calculate EPS ttm for each of the years we have available
# EPS_ttm < - round(temp_ttm_df$Value / temp_ttm_df2$Value, digits = 2)
#
# # Calculate the PE ratio for each of the years we have avaailable
# PE_Ratio < - round(tempClosePrice$Close / EPS_ttm, digits = 2)
#
# # Create the PE data frame
# PE_df < - rbind(PE_df, cbind("Ticker" = ticker[i], "Date" = temp_ttm_df2$Date, "ClosePrice" = round(
#     tempClosePrice$Close, digits = 2), "NetIncome" = temp_ttm_df$Value,
#                                                                  "SharesOutstanding" = temp_ttm_df2$Value, "EPS" = EPS_ttm, "PE_Ratio" = PE_Ratio))
#
# PE_df < - rbind(PE_df, cbind("Ticker" = ticker[i], "Date" = MostRecentCloseDate, "ClosePrice" = round(
#     MostRecentClosePrice, digits=2), "NetIncome" = temp_ttm_df$Value[1],
#                                                                "SharesOutstanding" = temp_ttm_df2$Value[1], "EPS" =
# EPS_ttm[1], "PE_Ratio" = round(MostRecentClosePrice / EPS_ttm[1], digits=2)))
# }
# PE_df$Date < - as.Date(as.character(PE_df$Date))
# PE_df < - PE_df[order(PE_df$Ticker, PE_df$Date, decreasing = TRUE), ]
# PE_df$Ticker < - as.character(PE_df$Ticker)
# PE_df$ClosePrice < - as.numeric(as.character(PE_df$ClosePrice))
# PE_df$NetIncome < - as.numeric(as.character(PE_df$NetIncome))
# PE_df$SharesOutstanding < - as.numeric(as.character(PE_df$SharesOutstanding))
# PE_df$EPS < - as.numeric(as.character(PE_df$EPS))
# PE_df$PE_Ratio < - as.numeric(as.character(PE_df$PE_Ratio))
#
# # Do not include the last EPS since that value is repeat from last calculated from annual financial statements
# TempPE_df < - PE_df[PE_df$Date != max(PE_df$Date), ]
#
# # Now perform the PE valuation model
# PEValuation_df < - data.frame()
# for (i in 1:length(ticker)){
#
# # Get the median PE ratio for the past years
# MedianPE_df < - PE_df[PE_df$Ticker == ticker[i],]
# MedianPE < - median(MedianPE_df$PE_Ratio)
#
# # Get the company's most recent reported EPS (ttm)
# EPS < - PE_df[PE_df$Ticker == ticker[i],]$EPS[1]
#
# # Calculate EPS growth rate
# temp.df < - TempPE_df[TempPE_df$Ticker == ticker[i],]
# linearModel < - lm(EPS
# ~ Date, data = temp.df)
# OneYearValue < - as.vector(((as.numeric(temp.df$Date[1]) + 365) * coefficients(linearModel)[2]) +
#                     coefficients(linearModel)[1])
# CurrentYearValue < - as.vector(((as.numeric(temp.df$Date[1])) * coefficients(linearModel)[2]) +
#                         coefficients(linearModel)[1])
# PEGrowthRate < - round((OneYearValue / CurrentYearValue) - 1, digits=3)
#
# # Get the close price of the stock
# tempPrice_df < - data.frame(
# try(getSymbols(ticker[i], from =Sys.Date()-5, auto.assign = FALSE, src='google'), silent = TRUE))
# colnames(tempPrice_df) < - sub(".+\\.", "", colnames(tempPrice_df))
# ClosePrice < - tempPrice_df$Close[nrow(tempPrice_df)]
#
# if (PEGrowthRate < 0 & ExpectedGrowthRate <= 0) {  # Apply the margin of safety on the growth rate
# PEConservative_GrowthRate < - PEGrowthRate * (1 + MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = PEGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                             "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                        "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                 "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
# } else if (ExpectedGrowthRate <= 0){
# PEConservative_GrowthRate < - PEGrowthRate * (1 - MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = PEGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                             "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                        "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                 "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
# } else {
# PEConservative_GrowthRate < - ExpectedGrowthRate * (1 - MarginSafety)
#
# # Perform the PE Valuation Model
# PE_Valuation < - MedianPE * EPS * (1 + PEConservative_GrowthRate) ^ 5
# NPV_PE_Valuation < - PE_Valuation / (1 + DiscountRate) ^ 5
#
# PEValuation_df < - rbind(PEValuation_df, cbind("Ticker" = ticker[
#                                                               i], "Median_PE" = MedianPE, "EPS_ttm" = EPS, "EPSGrowthRate" = ExpectedGrowthRate, "MarginSafety" = MarginSafety,
#                                                                                                                                                                   "EPS_ConservativeGrowthRate" = PEConservative_GrowthRate, "PE_Valuation" = round(
#     PE_Valuation, digits=3),
#                                                                                                                                                                                                                                              "PE_Valuation_Formula" = paste(
#     MedianPE, "*", EPS, "*(1+", PEConservative_GrowthRate, ")^5", sep=""),
#                                                                                                                                                                                                                                                                       "NPV_PE_Valuation" = round(
#     NPV_PE_Valuation, digits=2), "Most_Current_Stock_Price" = round(ClosePrice, digits=2)))
#
# }
# }
#
# # Conditonal Statements for the return function
# if (Get == "Plot_1"){
# # This plot will be used to compare the PE valuation vs the most recent stock price
#
# temp_df < - data.frame(cbind("Ticker"=as.character(PEValuation_df$Ticker), "PE_Valuation"=as.numeric(as.character(PEValuation_df$NPV_PE_Valuation)),
# "Most_Recent_Stock_Price"=as.numeric(as.character(PEValuation_df$Most_Current_Stock_Price))))
# temp_df < - melt(temp_df, id="Ticker")
#
# colnames(temp_df) < - c("Ticker", "Valuation Type", "Price")
# temp_df[, 1] < - as.character(temp_df[, 1])
# temp_df[, 2] < - as.character(temp_df[, 2])
# temp_df[, 3] < - as.numeric(as.character(temp_df[, 3]))
#
#
# ggplot(temp_df, aes(x=`Valuation Type`, y=Price, fill=`Valuation Type`, label=Price)) +
# geom_bar(stat = "identity", color = "gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("PE Multiple Valuation") + labs(x="Valuation Type", y="Value ($)") +
# theme(plot.title = element_text(hjust = 0.5))
#
# } else if (Get == "Plot_2"){
# # Plot this to show earnings per share
#
# temp_df < - data.frame(cbind("Date"=as.character((TempPE_df$Date)), "Ticker"=as.character(TempPE_df$Ticker), "EPS"=as.numeric(as.character(TempPE_df$EPS))))
#
# temp_df < - melt(temp_df, id=c("Ticker", "Date"))
# temp_df[, 1] < - as.character(temp_df[, 1])
# temp_df[, 2] < - as.Date(as.character(temp_df[, 2]))
# temp_df[, 3] < - as.character(temp_df[, 3])
# temp_df[, 4] < - as.numeric(as.character(temp_df[, 4]))
#
# ggplot(temp_df, aes(x = Date, y = value, color = variable, label = round(value, digits = 2))) + geom_point(size=1.8) + geom_line(size=1.3) +
# facet_grid(~ Ticker) + geom_text(vjust=-1.4, size=3) + ggtitle("Earnings Per Share (EPS)") +
# labs(x="Date", y="EPS") + theme(plot.title = element_text(hjust = 0.5))
#
# } else if (Get == "Plot_3"){
#
# # Plot this to show PE ratio
#
# temp_df < - data.frame(cbind("Date"=as.character((PE_df$Date)), "Ticker"=as.character(PE_df$Ticker), "Price_Earnings_Ratio"=as.numeric(as.character(PE_df$PE_Ratio))))
#
# temp_df < - melt(temp_df, id=c("Ticker", "Date"))
# temp_df[, 1] < - as.character(temp_df[, 1])
# temp_df[, 2] < - as.Date(as.character(temp_df[, 2]))
# temp_df[, 3] < - as.character(temp_df[, 3])
# temp_df[, 4] < - as.numeric(as.character(temp_df[, 4]))
#
# ggplot(temp_df, aes(x = Date, y = value, color = variable, label = round(value, digits = 2))) + geom_point(size=1.8) + geom_line(size=1.3) +
# facet_grid(~ Ticker) + geom_text(vjust=-1.4, size=3) + ggtitle("PE Ratio") +
# labs(x="Date", y="PE") + theme(plot.title = element_text(hjust = 0.5))
#
# } else if (Get == "Table_1"){
# # This table will be on the analysis tab, used to show the metrics to calculate EPS and the PE ratio
# PE_df
#
# } else if (Get == "Table_2"){
# # This table will be on the analysis tab, used to show how the PE Valuation method was calculated
# PEValuation_df
# }
#
# }
#
#
# ##Function for Miscellaneous metrics
# Misc_Metrics < - function(Get, Get2, ticker){
# ticker < - as.vector(strsplit(ticker, ",")[[1]])
# # Load main dataset function
# data_finaldf < - data_finaldf(ticker)
#
# if (Get == "CashEquivalents"){
# # Show cash and cash equivalents over time
# Cash_Equivalents_df < - data.frame()
# for (i in 1:length(ticker)){
# CashEquivalents_temp < - data_finaldf[data_finaldf$Ticker == ticker[i] & data_finaldf$Metric == "Cash & Equivalents",][,
#     3:5]
# Cash_Equivalents_df < - rbind(Cash_Equivalents_df, CashEquivalents_temp)
#
# }
#
# Cash_Equivalents_df[, 1] < - as.character(Cash_Equivalents_df[, 1])
# Cash_Equivalents_df[, 2] < - as.numeric(as.character(Cash_Equivalents_df[, 2]))
# Cash_Equivalents_df[, 3] < - as.character(Cash_Equivalents_df[, 3])
#
# if (Get2 == "Table"){
# Cash_Equivalents_df
# } else if (Get2 == "Plot"){
#
# ggplot(Cash_Equivalents_df, aes(x=as.Date(Date), y = Value, fill = Ticker, label = Value)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Cash & Cash Equivalents") + labs(x="Date", y="Cash & Cash Equivalents") +
# theme(plot.title = element_text(hjust=0.5))
# }
#
# } else if (Get == "BookValueShare"){
#
# # Show book value per share over time
# ShareHoldersEquity_df < - data.frame()
# for (i in 1:length(ticker)){
# SharesOutstanding < - data_finaldf[data_finaldf$Metric == "Total Common Shares Outstanding" & data_finaldf$Ticker ==
#                                                                                                            ticker[i],]
# SharesOutstanding < - SharesOutstanding[order(SharesOutstanding$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets",]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities",]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[
#     order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# BookValue_Share < - round(ShareholdersEquity / SharesOutstanding$Value, digits = 3)
#
# ShareHoldersEquity_df < - rbind(ShareHoldersEquity_df, cbind("Ticker" = ticker[
#                                                                             i], "Date" = SharesOutstanding$Date, "Total_Assets" = ShareholdersEquity_Assets$Value, "Total_Liabilities" = ShareholdersEquity_Liabilities$Value,
#                                                                                                                                                                                                                         "ShareHolders_Equity" = ShareholdersEquity, "BookValue_Share" = BookValue_Share))
# }
#
# ShareHoldersEquity_df[, 1] < - as.character(ShareHoldersEquity_df[, 1])
# ShareHoldersEquity_df[, 2] < - as.Date(as.character(ShareHoldersEquity_df[, 2]))
# ShareHoldersEquity_df[, 3] < - as.numeric(as.character(ShareHoldersEquity_df[, 3]))
# ShareHoldersEquity_df[, 4] < - as.numeric(as.character(ShareHoldersEquity_df[, 4]))
# ShareHoldersEquity_df[, 5] < - as.numeric(as.character(ShareHoldersEquity_df[, 5]))
# ShareHoldersEquity_df[, 6] < - as.numeric(as.character(ShareHoldersEquity_df[, 6]))
#
# if (Get2 == "Table"){
# ShareHoldersEquity_df
# } else if (Get2 == "Plot"){
#
# ggplot(ShareHoldersEquity_df, aes(x=Date, y=BookValue_Share, fill=Ticker, label=BookValue_Share)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Book Value per Share") + labs(x="Date", y="Book Vaue per Share") +
# theme(plot.title = element_text(hjust=0.5))
# }
#
# } else if (Get == "NetMargin"){
#
# # Show net margin over time
# NetMargin_df < - data.frame()
# for (i in 1:length(ticker)){
# Revenue_df < - data_finaldf[data_finaldf$Metric == "Total Revenue" & data_finaldf$Ticker == ticker[i],]
# Revenue_df < - Revenue_df[order(Revenue_df$Date, decreasing = TRUE), ]
#
# NetIncome_df < - data_finaldf[data_finaldf$Metric == "Net Income" & data_finaldf$Ticker == ticker[i],]
# NetIncome_df < - NetIncome_df[order(NetIncome_df$Date, decreasing = TRUE), ]
#
# NetMargin < - round(NetIncome_df$Value / Revenue_df$Value, digits = 3)
#
# NetMargin_df < - rbind(NetMargin_df, cbind("Ticker" = ticker[i], "Date" = Revenue_df$Date, "Revenue" = Revenue_df$Value,
#                                                                                                                   "Net_Income" = NetIncome_df$Value, "NetMargin" = NetMargin))
# }
#
# NetMargin_df[, 1] < - as.character(NetMargin_df[, 1])
# NetMargin_df[, 2] < - as.Date(as.character(NetMargin_df[, 2]))
# NetMargin_df[, 3] < - as.numeric(as.character(NetMargin_df[, 3]))
# NetMargin_df[, 4] < - as.numeric(as.character(NetMargin_df[, 4]))
# NetMargin_df[, 5] < - as.numeric(as.character(NetMargin_df[, 5]))
#
# if (Get2 == "Table"){
# NetMargin_df
# } else if (Get2 == "Plot"){
#
# ggplot(NetMargin_df, aes(x=Date, y=NetMargin, fill=Ticker, label=NetMargin)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Net Margin") + labs(x="Date", y="Net Margin") +
# theme(plot.title = element_text(hjust=0.5))
# }
#
# } else if (Get == "ReturnEquity"){
#
# # Show return on equity over time
# ReturnEquity_df < - data.frame()
# for (i in 1:length(ticker)){
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets" & data_finaldf$ttm != "Quarterly Data",]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities" & data_finaldf$ttm != "Quarterly Data",]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[
#     order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# NetIncome_df < - data_finaldf[data_finaldf$Metric == "Net Income" & data_finaldf$Ticker == ticker[i],]
# NetIncome_df < - NetIncome_df[NetIncome_df$Date <= max(ShareholdersEquity_Assets$Date), ]
# NetIncome_df < - NetIncome_df[order(NetIncome_df$Date, decreasing = TRUE), ]
#
# ReturnEquity < - round(NetIncome_df$Value / ShareholdersEquity, digits = 3)
#
# ReturnEquity_df < - rbind(ReturnEquity_df, cbind("Ticker" = ticker[
#                                                                 i], "Date" = ShareholdersEquity_Assets$Date, "Net_Income" = NetIncome_df$Value, "Total_Assets" = ShareholdersEquity_Assets$Value,
#                                                                                                                                                                                            "Total_Liabilities" = ShareholdersEquity_Liabilities$Value, "ShareHolders_Equity" = ShareholdersEquity, "ReturnEquity" = ReturnEquity))
#
# }
#
# ReturnEquity_df[, 1] < - as.character(ReturnEquity_df[, 1])
# ReturnEquity_df[, 2] < - as.Date(as.character(ReturnEquity_df[, 2]))
# ReturnEquity_df[, 3] < - as.numeric(as.character(ReturnEquity_df[, 3]))
# ReturnEquity_df[, 4] < - as.numeric(as.character(ReturnEquity_df[, 4]))
# ReturnEquity_df[, 5] < - as.numeric(as.character(ReturnEquity_df[, 5]))
# ReturnEquity_df[, 6] < - as.numeric(as.character(ReturnEquity_df[, 6]))
# ReturnEquity_df[, 7] < - as.numeric(as.character(ReturnEquity_df[, 7]))
#
# if (Get2 == "Table"){
# ReturnEquity_df
# } else if (Get2 == "Plot"){
#
# ggplot(ReturnEquity_df, aes(x=Date, y=ReturnEquity, fill=Ticker, label=ReturnEquity)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Return on Equity") + labs(x="Date", y="Return on Equity") +
# theme(plot.title = element_text(hjust=0.5))
# }
#
# } else if (Get == "DebtEquity"){
# # Show long term debt to equity over time
# DebtEquity_df < - data.frame()
# for (i in 1: length(ticker)){
# LongTermDebt_df < - data_finaldf[data_finaldf$Metric == "Total Long Term Debt" & data_finaldf$Ticker == ticker[i],]
# LongTermDebt_df < - LongTermDebt_df[order(LongTermDebt_df$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Assets < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Assets",]
# ShareholdersEquity_Assets < - ShareholdersEquity_Assets[order(ShareholdersEquity_Assets$Date, decreasing = TRUE), ]
#
# ShareholdersEquity_Liabilities < - data_finaldf[data_finaldf$Ticker == ticker[
#     i] & data_finaldf$FinancialStatement == "BalanceSheet" & data_finaldf$Metric == "Total Liabilities",]
# ShareholdersEquity_Liabilities < - ShareholdersEquity_Liabilities[
#     order(ShareholdersEquity_Liabilities$Date, decreasing = TRUE), ]
#
# ShareholdersEquity < - ShareholdersEquity_Assets$Value - ShareholdersEquity_Liabilities$Value
#
# DebtEquity < - round(LongTermDebt_df$Value / ShareholdersEquity, digits = 3)
#
# DebtEquity_df < - rbind(DebtEquity_df, cbind("Ticker" = ticker[
#                                                             i], "Date" = ShareholdersEquity_Assets$Date, "LongTermDebt" = LongTermDebt_df$Value, "Total_Assets" = ShareholdersEquity_Assets$Value,
#                                                                                                                                                                                             "Total_Liabilities" = ShareholdersEquity_Liabilities$Value, "ShareHolders_Equity" = ShareholdersEquity, "DebtToEquity" = DebtEquity))
#
# }
#
# DebtEquity_df[, 1] < - as.character(DebtEquity_df[, 1])
# DebtEquity_df[, 2] < - as.Date(as.character(DebtEquity_df[, 2]))
# DebtEquity_df[, 3] < - as.numeric(as.character(DebtEquity_df[, 3]))
# DebtEquity_df[, 4] < - as.numeric(as.character(DebtEquity_df[, 4]))
# DebtEquity_df[, 5] < - as.numeric(as.character(DebtEquity_df[, 5]))
# DebtEquity_df[, 6] < - as.numeric(as.character(DebtEquity_df[, 6]))
# DebtEquity_df[, 7] < - as.numeric(as.character(DebtEquity_df[, 7]))
#
# if (Get2 == "Table"){
# DebtEquity_df
# } else if (Get2 == "Plot"){
#
# ggplot(DebtEquity_df, aes(x=Date, y=DebtToEquity, fill=Ticker, label=DebtToEquity)) +
# geom_bar(stat="identity", width=100, color="gray") + facet_grid(~ Ticker) + geom_text(vjust=-.25) +
# ggtitle("Long Term Debt to Equity Ratio") + labs(x="Date", y="Long Term Debt to Equity") +
# theme(plot.title = element_text(hjust=0.5))
# }
# }
# }
#
#
# ##Function to get the financial statements
# Financial_Statements < - function(ticker)
# {
#     ticker < - as.vector(strsplit(ticker, ",")[[1]])
# data_finaldf(ticker)
# }
#
#
# shinyServer(
#     function(input, output)
# {
#
#     ##Group these outputs for DCF Valuation Model Tab
#     output$DCF_Model.plot < - renderPlot({DCF_Valuation(Get="Plot_1",
#                                                         ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate, MarginSafety = input$MarginSafety,
#                                                                                                                                                  GrowthDeclineRate = input$GrowthDeclineRate, DiscountRate = input$DiscountRate, DCF_YearsProjection = input$DCF_YearsProjection,
#                                                                                                                                                                                                                                                              LongTermGrowthRate = input$LongTermGrowthRate)})
#
# output$DCF_Model.plot2 < - renderPlot({DCF_Valuation(Get="Plot_2",
#                                                      ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate, MarginSafety = input$MarginSafety,
#                                                                                                                                               GrowthDeclineRate = input$GrowthDeclineRate, DiscountRate = input$DiscountRate, DCF_YearsProjection = input$DCF_YearsProjection,
#                                                                                                                                                                                                                                                           LongTermGrowthRate = input$LongTermGrowthRate)})
#
# output$DCF_Model.table < - renderDataTable({DCF_Valuation(Get="Table_1",
#                                                           ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate, MarginSafety = input$MarginSafety,
#                                                                                                                                                    GrowthDeclineRate = input$GrowthDeclineRate, DiscountRate = input$DiscountRate, DCF_YearsProjection = input$DCF_YearsProjection,
#                                                                                                                                                                                                                                                                LongTermGrowthRate = input$LongTermGrowthRate)})
#
# output$DCF_Model.table2 < - renderDataTable({DCF_Valuation(Get="Table_2",
#                                                            ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate, MarginSafety = input$MarginSafety,
#                                                                                                                                                     GrowthDeclineRate = input$GrowthDeclineRate, DiscountRate = input$DiscountRate, DCF_YearsProjection = input$DCF_YearsProjection,
#                                                                                                                                                                                                                                                                 LongTermGrowthRate = input$LongTermGrowthRate)})
#
#
# ##Group these output for PE Valuation Model Tab
# output$PE_Model.plot < - renderPlot(
#     {PE_Valuation(Get="Plot_1", ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate,
#                                                                                 MarginSafety = input$MarginSafety, DiscountRate = input$MarginSafety)})
#
# output$PE_Model.plot2 < - renderPlot(
#     {PE_Valuation(Get="Plot_2", ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate,
#                                                                                 MarginSafety = input$MarginSafety, DiscountRate = input$MarginSafety)})
#
# output$PE_Model.table < - renderDataTable(
#     {PE_Valuation(Get="Table_1", ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate,
#                                                                                  MarginSafety = input$MarginSafety, DiscountRate = input$MarginSafety)})
#
# output$PE_Model.table2 < - renderDataTable(
#     {PE_Valuation(Get="Table_2", ticker=input$ticker, ExpectedGrowthRate = input$ExpectedGrowthRate,
#                                                                                  MarginSafety = input$MarginSafety, DiscountRate = input$MarginSafety)})
#
#
#
# ##Group these output for the Fundamental Analysis Tab
# output$Cash_Equivalents.plot < - renderPlot({Misc_Metrics(Get="CashEquivalents", Get2="Plot", ticker=input$ticker)})
#
# output$Book_Value.plot < - renderPlot({Misc_Metrics(Get="BookValueShare", Get2="Plot", ticker=input$ticker)})
#
# output$Net_Margin.plot < - renderPlot({Misc_Metrics(Get="NetMargin", Get2="Plot", ticker=input$ticker)})
#
# output$Return_Equity.plot < - renderPlot({Misc_Metrics(Get="ReturnEquity", Get2="Plot", ticker=input$ticker)})
#
# output$Debt_Equity.plot < - renderPlot({Misc_Metrics(Get="DebtEquity", Get2="Plot", ticker=input$ticker)})
#
#
# output$Cash_Equivalents.table < - renderDataTable(
#     {Misc_Metrics(Get="CashEquivalents", Get2="Table", ticker=input$ticker)})
#
# output$Book_Value.table < - renderDataTable({Misc_Metrics(Get="BookValueShare", Get2="Table", ticker=input$ticker)})
#
# output$Net_Margin.table < - renderDataTable({Misc_Metrics(Get="NetMargin", Get2="Table", ticker=input$ticker)})
#
# output$Return_Equity.table < - renderDataTable({Misc_Metrics(Get="ReturnEquity", Get2="Table", ticker=input$ticker)})
#
# output$Debt_Equity.table < - renderDataTable({Misc_Metrics(Get="DebtEquity", Get2="Table", ticker=input$ticker)})
#
#
# ##Group this output by oneself, for Financial statements tab
# output$FinanceData.table < - renderDataTable({Financial_Statements(ticker=input$ticker)})
# })
