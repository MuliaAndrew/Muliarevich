**How to create SSH key**
	Open Bash console
	Type 'key-gen -t ed25519 -C "user_name@gmail.com"'

**How to add SSH key to Github accaunt**
	Go to github.com then sign in
	Open user settings -> SSH GPG keys
	click 'Add SSH key'
	copy your public key from its file and past into field 'key'

**How to clone repository from Github**
	Open your repository on github.com
	Copy its SSH adress
	Open bash console
	type git clone then past copied adress
