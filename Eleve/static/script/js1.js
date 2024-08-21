
// Graphique du nombre d'étudiants

const ctx = document.getElementById('genderChart').getContext('2d');

const genderChart = new Chart(ctx, {
    type: 'pie', // Vous pouvez changer cela en 'pie' ou 'doughnut' pour d'autres types de graphiques
    data: {
        labels: ['Hommes', 'Femmes'],
        datasets: [{
            label: 'Répartition par Sexe',
            data: [60, 40], // 60% Hommes, 40% Femmes
            backgroundColor: [
                'rgba(54, 162, 235, 0.6)', // Couleur pour les Hommes
                'rgba(255, 99, 132, 0.6)'  // Couleur pour les Femmes
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                position: 'right',
            }
        }
    }
});
