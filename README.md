Regex Sampler
---

Simple commandline utility to generate samples uniformly over the space of strings matching a provided regular expression. Useful for spoofing input to programs!

## Example:
We can generate a stream of fake JSON data representing people and their emails!
```
$	./resample.py ./resample.py '{ "name":"(\w+) (\w+)", "email": "\1_\2@\w+.(edu|com|org)"}'

{ "name":"R TWER", "email": "R_TWER@PVRcyR)com"}
{ "name":"mwGwTOWKRXs GIGY", "email": "mwGwTOWKRXs_GIGY@FvERutwS]org"}
{ "name":"igUMTrViMt oTkFPAySfn", "email": "igUMTrViMt_oTkFPAySfn@kQekedu"}
{ "name":"MtvMHGBi R", "email": "MtvMHGBi_R@UCPbGDjJai&com"}
{ "name":"fbMyddFkTRP QeH", "email": "fbMyddFkTRP_QeH@ekmjacom"}
{ "name":"vO devQkFbORdi", "email": "vO_devQkFbORdi@LaAPfnmMcnTZlYorg"}
{ "name":"khT BoWvCONzyeOYoNgasncZnU", "email": "khT_BoWvCONzyeOYoNgasncZnU@kV-com"}
{ "name":"TmEU TvjeB", "email": "TmEU_TvjeB@pMMnvdcom"}
{ "name":"rzjoN jkpSd", "email": "rzjoN_jkpSd@qTLvRUedu"}
{ "name":"pgzQ fz", "email": "pgzQ_fz@Shtedu"}



```

## Soon
- Better commandline interface
