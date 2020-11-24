# O(N)
def average_celsius(fahrenheit_readings)
# Collect Celsius numbers here:
 celsius_numbers = []
# # Convert each reading to Celsius and add to array:
 fahrenheit_readings.each do |fahrenheit_reading |
   celsius_conversion = (fahrenheit_reading - 32) / 1.8
   celsius_numbers.push(celsius_conversion)
 end
# # Get sum of all Celsius numbers:
 sum = 0.0
 celsius_numbers.each do |celsius_number|
 sum += celsius_number
 end
# # Return mean average:
 return sum / celsius_numbers.length
end
