var mix = {
	methods: {
		signUp () {
			const name = document.querySelector('#name').value
			const username = document.querySelector('#login').value
			const password = document.querySelector('#password').value
			this.postData(
				'/api/sign-up/',
				JSON.stringify({ name, username, password }),
				{
        			'Content-Type': 'application/json'
    				}
				)
				.then(({ data, status }) => {
					location.assign(`/`)
				})
		}
	},
	mounted() {
	},
	data() {
		return {}
	}
}
