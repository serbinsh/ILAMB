from numpy import asarray,ones,copy as npcopy

__all__ = ['spm','mph','hpd','mpy','dpy_noleap','dpy_gregorian','dpy_360','dpm_noleap','dpm_gregorian','dpm_360','g_per_Pg','g_per_kg','Ar_molar_mass','C_molar_mass','N_molar_mass','O_molar_mass','CO2_molar_mass','dry_air_molar_mass','dry_air_mass','dry_air_moles','co2_g_per_ppm','co2_ppm_per_kg','co2_ppm_per_C_Pg','biomes']

# Time constants
spm              = 60.     # seconds per minute
mph              = 60.     # minutes per hour
hpd              = 24.     # hours per day
mpy              = 12.     # months per year
dpy_noleap       = 365.0   # days per year (for no leap year calendars)
dpy_gregorian    = 365.25  # days per year
dpy_360          = 360.0   # days per year (for 30 days/month)
dpm_noleap       = asarray([31,28,31,30,31,30,31,31,30,31,30,31],dtype='float') # days per month
dpm_gregorian    = npcopy(dpm_noleap) ; dpm_gregorian[1] = dpm_gregorian[1] + 0.25
dpm_360          = ones(mpy)*30.

# Mass unit conversions
g_per_Pg         = 1e+15   # grams per Pg
g_per_kg         = 1e+3    # grams per kg

# Chemical constants
Ar_molar_mass    = 39.948  # grams per mole
C_molar_mass     = 12.0107 # grams per mole
N_molar_mass     = 14.0067 # grams per mole
O_molar_mass     = 15.9994 # grams per mole
CO2_molar_mass   = C_molar_mass + 2. * O_molar_mass # grams per mole

# Atmospheric constants
dry_air_molar_mass = 0.78084*2.*N_molar_mass + 0.20946*2.*O_molar_mass + 0.00934*Ar_molar_mass + 0.00039445*CO2_molar_mass # grams per mole
dry_air_mass       = 5.1352e+21 # grams
dry_air_moles      = dry_air_mass / dry_air_molar_mass
co2_g_per_ppm      = dry_air_moles * CO2_molar_mass / 1.e+6
co2_ppm_per_kg     = g_per_kg / co2_g_per_ppm
co2_ppm_per_C_Pg   = g_per_Pg / co2_g_per_ppm * CO2_molar_mass/C_molar_mass

# Earth constants
earth_rad = 6.371e6 # meters

convert = {}
convert["co2"] = {}
convert["co2"]["1e-6"] = {"kg"  :co2_ppm_per_kg, "1e-6": 1.}
convert["co2"]["kg"]   = {"1e-6":1./co2_ppm_per_kg, "kg": 1.}
convert["gpp"] = {}
convert["gpp"]["kg m-2 s-1"] = {"g m-2 s-1":1e-3,"kg m-2 s-1":1.}
convert["gpp"]["g m-2 s-1"]  = {"kg m-2 s-1":1e+3,"g m-2 s-1":1.}

biomes = {}
biomes["global.large"] = ((-89.75, 89.75),(-179.75, 179.75))
biomes["global"]       = ((-60.25, 80.25),(-179.75, 179.75))
biomes["amazon"]       = ((-12.25,  6.75),(- 75.25,- 50.25))
biomes["alaska"]       = (( 50.25, 75.25),(-170.25,-130.25))
biomes["australia"]    = ((-50.25,-10.25),( 100.25, 160.25))
biomes["bona"]         = (( 49.75, 79.75),(-170.25,- 60.25))
biomes["tena"]         = (( 30.25, 49.75),(-125.25,- 80.25))
biomes["ceam"]         = ((  9.75, 30.25),(-115.25,- 80.25))
biomes["nhsa"]         = ((  0.25,  9.75),(- 80.25,- 50.25))
biomes["shsa"]         = ((-59.75,  0.25),(- 80.25,- 40.25))
biomes["euro"]         = (( 40.25, 70.25),(- 10.25,  30.25))
biomes["mide"]         = (( 20.25, 40.25),(- 10.25,  60.25))
biomes["nhaf"]         = ((  0.25, 20.25),(- 20.25,  45.25))
biomes["shaf"]         = ((-34.75,  0.25),(  10.25,  45.25))
biomes["boas"]         = (( 54.75, 70.25),(  30.25, 179.75))
biomes["ceas"]         = (( 30.25, 54.75),(  30.25, 135.25))
biomes["seas"]         = (( 10.25, 30.25),(  65.25, 120.25))
biomes["eqas"]         = ((-10.25, 10.25),(  99.75, 150.25))
biomes["aust"]         = ((-34.75,-10.25),( 124.75, 154.75))