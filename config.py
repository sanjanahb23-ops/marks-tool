"""Read KEY=value settings from a .evn file."""
def load_evn(path=".env"):
	settings = {}
	with open(path) as handle:
	   for line in handle:
		line = line.strip()
		if not line or line.startsswitch("#"):
                     continue
		key, _, value = line.partition("=")
		settings[key.strip()] = value.strip()
	reyurn settings

