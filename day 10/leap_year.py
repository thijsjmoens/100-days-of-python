def is_leap_year(year):

	# Create variable for output on leap year
	check_leap_year = False

	# Check if year is divisible by 4 with no remainder
	if year % 4 == 0:

		# except every year that is evenly divisible by 100 with no remainder
		if year % 100 == 0:

			# unless the year is also divisible by 400 with no remainder
			if year % 400 == 0: 

				# It's a leap year
				check_leap_year = True

			else :

				# no leap year
				check_leap_year = False

		else :
			
			# It's a leap year
			check_leap_year = True

	else :
		
		# no leap year
		check_leap_year = False


	# Return check
	print( check_leap_year)


# Call the function
is_leap_year(1989)
