const modalSelected = document.getElementById('modal')
const showWinnerBtn = document.getAnimations('show-winner-btn')
const modalCloseBtn = document.getAnimations('close-btn')

const handleShowModal = modalSelected.classList.add('show')
const handleCloseModal =  modalSelected.classList.add('close')

showWinnerBtn(addEventListener('click',handleShowModal))
modalCloseBtn(addEventListener('click',handleCloseModal))

//HTML frame needed!!
const winner = player.name// get player name from DB by playerID
//modal heading update
const modalHeaderSelected = document.getElementById('modal-header') //Id depend on HTML
const modalImgSelected = document.getElementById('modal-img') //Id depend on HTML

modalHeaderSelected.innerHTML = `${winner}`
modalImgSelected.setAttribute('src','assets/img/winner/winnerModal.png')