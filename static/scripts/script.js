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

const typed = new Typed('.multiple.text', {
    strings: ['Frontend Developer', 'Network Security', 'Cyber security', 'System Administration'],
    typespeed: 80,
    backSped: 80,
    backDelay: 1200,
    loop: true,
});



 document.querySelectorAll('.download-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                const textSpan = this.querySelector('.btn-text');
                
                // Toggle CSS states
                this.classList.add('is-loading');
                textSpan.textContent = "Downloading...";
                
                // Return button to active state after download stream hands off
                setTimeout(() => {
                    this.classList.remove('is-loading');
                    textSpan.textContent = "Download DOCX";
                }, 3000);
            });
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
