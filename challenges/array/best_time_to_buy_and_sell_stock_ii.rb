def maxProfit(prices)
  profit = 0
  (1...prices.size).each do |i|
    profit += prices[i] - prices[i - 1] if prices[i] > prices[i - 1]
  end
  profit
end
