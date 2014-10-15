Regex Sampler
---

Simple commandline utility to generate samples uniformly over the space of strings matching a provided regular expression. Useful for spoofing input to programs!

## Example:
We can generate a stream of fake JSON data representing people and their emails!
```
$	echo '{ email: "\w+\d*@\w+.com", name: "\w+" }' | ./resample.py 

{ email: "cT90@EySKdD.com", name: "h" }
{ email: "ftfgEbIwBA0347958@EmBgmDtoL.com", name: "eIbTwd" }
{ email: "TgRATh747@HKQsiu.com", name: "UEmtWLK" }
{ email: "iVI89633@DQPH.com", name: "RGcZ" }
{ email: "CAddUKBd780717279@PCVmkuEgt.com", name: "SBvkcrOUf" }
{ email: "nyNmatC3243374846@vPr.com", name: "NRUtPXu" }
{ email: "cEryY8@gIs.com", name: "xPpifmJ" }
{ email: "WJkYLKt9335272938@moz.com", name: "IGspfNufnm" }
{ email: "vFIsqS546266261@GyijjP.com", name: "s" }
{ email: "yH3336054@yyggKBo.com", name: "XpqZ" }

```

## Soon
Lots of TODOs here.

 - Sampling ```*``` patterns from a geometric distribution rather than a uniform over a fixed number of repititions (default is 10)
 - Fixed and range repitition patterns ```{m[,n]}```
 - Or ```|``` patterns
 - Any ```[]``` patterns
 - Grouping with ```()```
 - Better commandline usability
