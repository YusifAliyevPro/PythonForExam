# Ədədi silsilədə n+1 həddinin cəmini çap edən proqram
a1 = int(input("Ilk həddi daxil edin: "))
d = int(input("Silsilə fərqini daxil edin: "))
n = int(input("Hansı həddə qədər cəmləmək istəyirsiz?: "))+1

s = (2*a1+d*(n-1))*n/2
print(s)

# Input:
# Ilk həddi daxil edin: 5
# Silsilə fərqini daxil edin: 5
# Hansı həddə qədər cəmləmək istəyirsiz?: 3

# Output: 50.0
