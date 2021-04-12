
Chart.defaults.font.size = 20;

function displayGenre(men, womans) {
	var genre = document.getElementById("genre").getContext("2d");
	const data = {
		labels: [
		  'الرجال',
		  'النساء',
		],
		datasets: [{
		  label: 'My First Dataset',
		  data: [men, womans],
		  backgroundColor: [
			'rgb(255, 99, 132)',
			'rgb(54, 162, 235)',
		  ],
		  hoverOffset: 5
		}]
	  };
	  const config = {
		type: 'pie',
		data: data,
		options: {
		}
	  };
	var genrePie = new Chart(genre,config);

}