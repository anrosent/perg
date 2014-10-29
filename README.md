Regex Sampler
---

Simple commandline utility to generate samples uniformly over the space of strings matching a provided regular expression. Useful for spoofing input to programs!

## Example:
We can generate a stream of fake JSON data representing people and their emails!
```
$	./resample.py '{ email: "\w+\d*@\w+\.(com|edu|org)", name: "\w+" }' 

{ email: "t@ltfiSrdbsufNCGEn.com", name: "Bm Gsiclruqqmoqcoshafggffnzbq" }
{ email: "ZAfBiJzQMmnvwuh@Tlh.com", name: "Oo Uhcapep" }
{ email: "dgXvFRVeBnxjqmcp@uppie.edu", name: "Vpcamqvkmemrdmt Mmwuclzqsecmoce" }
{ email: "xfPySMslEzdYgx@xIVkXYpc.org", name: "Welugkwrm Isecvrimkseem" }
{ email: "rbRblIQoT@mQgESyvwO.com", name: "Bbsh Jhmmjpwljdgb" }
{ email: "seMxENYfDCV@yJQPjiNJt.org", name: "Dkwpriliosfgcky Hguixmfcovq" }
{ email: "VfKyFwQFDTwcSm@wgMtb.org", name: "Kxebp Jnacpdwsslwwzgsfskrj" }
{ email: "VyCkUHhEkALWsVz@vOsgKBJesbB.com", name: "Gjkpzreyw Turri" }
{ email: "cBOP@KaGxv.org", name: "Zjpphghjxosufhjwyoq Qfuyqeakqbppww" }
{ email: "pFpGbEvrljEbZ@pknRANquxDcUz.com", name: "Xvqmkdkryb Eyuts" }


```

## Soon
- Better commandline interface
- Add proper sampling for the many subpattern ```(?``` variants (backreferences most important)
- Add geometric sampling over integers for ```*``` and ```+``` repeats instead of uniform over smaller range
