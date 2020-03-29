
// dropbox.com/developers
import { Dropbox } from 'Dropbox'

const dbx = new Dropbox({

	accessToken: 'tPyMKhZnPXAAAAAAAAAAYCdRfTiboexqwV-KRpPzVgr6pukQNFFwOG68F0_kQ6Tz',
	fetch
})

// http://dropbox.github.io/dropbox-sdk-js/Dropbox.html

const fileListElem = document.querySelector('.js-file-list')

dbx.filesListFolder({

	path: ''
}).then(res => console.log(res))