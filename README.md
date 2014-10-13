Regex Sampler
---

Simple commandline utility to generate samples uniformly over the space of strings matching a provided regular expression. Useful for spoofing input to programs!

## Example:
We can generate a stream of fake JSON data representing people and their emails!
```
$	echo '{ email: "\w+\d*@\w+.com", name: "\w+" }' | ./resample.py 

{ email: "TSyHofvq@iBApYEvxL.com", name: "aN" }
{ email: "NaKhJWqYrZfHxzwpPB@oqBUZhOqe.com", name: "ItfUes" }
{ email: "ynlQ@bqIk.com", name: "K" }
{ email: "HSmxMMdgSj@KnYjrvRZE.com", name: "KtUcZJc" }
{ email: "JnuTjZbCEy@j.com", name: "Ee" }
{ email: "mJGXNzjeBYSBzQ@LPIVpH.com", name: "dpSg" }
{ email: "lHWGvJVLrZaWM@OebmnGZPF.com", name: "mjHEyXqfp" }
{ email: "lbzyh@RE.com", name: "BgtdG" }
{ email: "jNYcjkMXaiiH@sOf.com", name: "k" }
{ email: "RKpNWVxDMwh@sEHvPk.com", name: "adq" }

```

## Soon
Lots of TODOs here.

 - Sampling ```*``` patterns from a geometric distribution rather than a uniform over a fixed number of repititions (default is 10)
 - Fixed and range repitition patterns ```{m[,n]}```
 - Or ```|``` patterns
 - Any ```[]``` patterns
 - Grouping with ```()```
 - Better commandline usability
