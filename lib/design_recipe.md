

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

<!-- input parameter string `YYYY-MM-DD`
store the date -->


As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).
<!-- 
check the difference between todays date and date of birth
convert it to years
access denied for 16 year -->


As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

<!-- 
check the difference between todays date and date of birth
convert it to years
access granted for 16 year -->