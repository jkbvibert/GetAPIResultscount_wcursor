# GetAPIResultscount_wcursor
This script iterates through the results of an API call and grabs the count of each resultset by iterating through the cursors and adding up the total result count.

This was helpful at the time as the API we were using couldn't handle very high limit values so we had to walk through the results manually.

An issue was being diagnosed with this scripts as the value returned by a count(*) query returned a different number of results compared to how many results returned when iterating through them one-by-one.
