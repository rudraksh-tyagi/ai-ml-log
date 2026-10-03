monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Nov"])  # Output: November   
print(monthConversion.get("luv" , "not a valid key"))  # Output: December
print(monthConversion.keys()) 
print(monthConversion.values())
print(monthConversion.items())  
monthConversion.update({"Dec": "December Updated"})
print(monthConversion["Dec"])  # Output: December Updated
monthConversion.pop("Jan")
print(monthConversion)  
monthConversion.clear()
print(monthConversion)  # Output: {}