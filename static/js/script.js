let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}

window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}

 const typed = new Typed(".mutiple-text", {
    strings: ['Frontend Web Development', 'Network Administration and security', 'Cyber security', 'System Administration'],
    typeSpeed: 80,
    backSped: 80,
    backDelay: 1200,
    loop: true,
    });



// Download 2
document.querySelectorAll('.download-btn').forEach(button => {

    button.addEventListener('click', function () {

        const spinner = this.querySelector('.spinner');
        const icon = this.querySelector('.download-icon');
        const text = this.querySelector('.btn-text');

        this.classList.add('loading');

        spinner.classList.remove('hidden');
        icon.classList.add('hidden');

        text.textContent = "Downloading...";

        setTimeout(() => {
            this.classList.remove('loading');

            spinner.classList.add('hidden');
            icon.classList.remove('hidden');

            text.textContent = "Download";
        }, 3000);
    });

});


// // DOWNLOAD 3
// document.addEventListener('DOMContentLoaded', () => {

//     document.querySelectorAll('.download-btn').forEach(button => {

//         button.addEventListener('click', function () {

//             if (this.dataset.loading === 'true') {
//                 return;
//             }

//             this.dataset.loading = 'true';

//             const spinner = this.querySelector('.spinner');
//             const icon = this.querySelector('.download-icon');
//             const success = this.querySelector('.success-icon');
//             const text = this.querySelector('.btn-text');
//             const progress = this.querySelector('.progress-bar');

//             icon.classList.add('hidden');
//             spinner.classList.remove('hidden');

//             this.classList.add('pointer-events-none');

//             text.textContent = 'Preparing File...';

//             progress.style.width = '25%';

//             setTimeout(() => {
//                 text.textContent = 'Generating Download...';
//                 progress.style.width = '60%';
//             }, 1000);

//             setTimeout(() => {
//                 text.textContent = 'Downloading...';
//                 progress.style.width = '90%';
//             }, 2000);

//             setTimeout(() => {

//                 spinner.classList.add('hidden');
//                 success.classList.remove('hidden');

//                 progress.style.width = '100%';

//                 text.textContent = 'Download Complete';

//                 this.classList.remove(
//                     'from-blue-600',
//                     'via-indigo-600',
//                     'to-purple-600'
//                 );

//                 this.classList.add(
//                     'from-green-500',
//                     'to-emerald-600'
//                 );

//             }, 3000);

//             setTimeout(() => {

//                 success.classList.add('hidden');
//                 icon.classList.remove('hidden');

//                 progress.style.width = '0%';

//                 text.textContent = 'Download DOCX';

//                 this.classList.remove(
//                     'from-green-500',
//                     'to-emerald-600'
//                 );

//                 this.classList.add(
//                     'from-blue-600',
//                     'via-indigo-600',
//                     'to-purple-600'
//                 );

//                 this.classList.remove('pointer-events-none');

//                 this.dataset.loading = 'false';

//             }, 6000);

//         });

//     });

// });




function openModal(modalId) {
    const modal = document.getElementById(modalId);

    modal.classList.remove('hidden');
    modal.classList.add('block');

    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);

    modal.classList.add('hidden');
    modal.classList.remove('block');

    document.body.style.overflow = 'auto';
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeModal('network_adminModal');
    }
});
