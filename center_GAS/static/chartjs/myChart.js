
Chart.defaults.font.size = 14;

function displayGenre(men, womans) {
	var genre = document.getElementById("genre").getContext("2d");
	const data = {
		labels: [
		  'الرجال',
		  'النساء',
		],
		datasets: [{
		  data: [men, womans],
		  backgroundColor: [
			'#57606f',
			'#ff6b81',
		  ],
		  hoverOffset: 4
		}]
	  };
	  const config = {
		type: 'pie',
		data: data,
		options: {
			responsive: true,
			plugins: {
			  legend: {
				position: 'bottom',
			  },
			  title: {
				display: true,
				text: 'عدد الرجال و النساء المسجلين في المركز'
			  }
			}
		  },
	  };
	var genrePie = new Chart(genre,config);
}


function displayAges(child, young, old) {
	var age = document.getElementById("age").getContext("2d");
	
	var mybarChart = new Chart(age, {
	  type: 'bar',
	  data: {
		labels: ['أقل من 20 سنة', 'ما بين 20 و 40 سنة', 'أكبر من 40 سنة'],
		datasets: [{
		  label: 'أقل من 20 سنة',
		  backgroundColor: "#26de81",
		  data: [child, 0, 0]
		}, {
		  label: 'ما بين 20 و 40 سنة',
		  backgroundColor: "#0fb9b1",
		  data: [0, young, 0]
		}, {
		  label: 'أكبر من 40 سنة',
		  backgroundColor: "#a5b1c2",
		  data: [0, 0, old]
		}]
	  },
	
	  options: {
		// responsive: true,
		plugins: {
		  legend: {
			position: 'top',
		  },
		  title: {
			display: true,
			text: 'تصنيف المسجلين في المركز حسب الأعمار'
		  }
		}
	  },
	});
}
	

function displayCards(hasCard, waitingCard) {
	var genre = document.getElementById("cards").getContext("2d");
	const data = {
		labels: [
		  'منجزة',
		  'طور الانجاز',
		],
		datasets: [{
		  data: [hasCard, waitingCard],
		  backgroundColor: [
			'#26de81',
			'#a5b1c2',
		  ],
		  hoverOffset: 4
		}]
	  };
	  const config = {
		type: 'pie',
		data: data,
		options: {
			responsive: true,
			plugins: {
			  legend: {
				position: 'bottom',
			  },
			  title: {
				display: true,
				text: 'طلبات بطاقات الأشخاص في وضعية إعاقة'
			  }
			}
		  },
	  };
	var genrePie = new Chart(genre,config);
}


function displayFood(hasFood, waitingFood) {
	var food = document.getElementById("food").getContext("2d");
	const data = {
		labels: [
		  'مستفيدون',
		  'لائحة الإنتضار',
		],
		datasets: [{
		  data: [hasFood, waitingFood],
		  backgroundColor: [
			'#26de81',
			'#a5b1c2',
		  ],
		  hoverOffset: 4
		}]
	  };
	  const config = {
		type: 'pie',
		data: data,
		options: {
			responsive: true,
			plugins: {
			  legend: {
				position: 'bottom',
			  },
			  title: {
				display: true,
				text: 'المشتركين في برنامج الطرد الغدائي'
			  }
			}
		  },
	  };
	var genrePie = new Chart(food,config);
}