function toggleSidebar() {
    document.getElementById('sidebar').classList.toggle('open');
    document.getElementById('sidebarOverlay').classList.toggle('active');
}

function navigateTo(cardId) {
    toggleSidebar();
    document.getElementById(cardId)?.scrollIntoView({ behavior: 'smooth' });
}

// Lógica de Respiración (Pausa Consciente)
const breathText = document.getElementById('breathText');
if (breathText) {
    setInterval(() => {
        breathText.innerText = (breathText.innerText === 'Inhala') ? 'Exhala' : 'Inhala';
    }, 4000);
}

// Interacción de Pilares Abecé (Touch/Click)
document.querySelectorAll('.pill-item-horizontal').forEach(pill => {
    pill.addEventListener('click', function() {
        this.classList.toggle('active');
    });
});
