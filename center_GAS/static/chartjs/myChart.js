
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
			'rgba(75, 192, 192, 0.3)',
			'rgba(255, 99, 132, 0.2)',
		  ],
		  hoverOffset: 4,
		  borderWidth: 1
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

function displayTypes(move, ear, eye, autism, late, trisomy) {
	var types = document.getElementById("types").getContext("2d");
	
	var mybarChart = new Chart(types, {
	  type: 'bar',
	  data: {
		labels: ['الثلاتي الصبغي 21' ,'التأخر الزمني','التوحد' ,'بصرية', 'سمعية', 'حركية'],
		datasets: [{
		//   label: 'My First Dataset',
		  data: [trisomy, late, autism, ear, eye, move],
		  backgroundColor: [
			'rgba(255, 99, 132, 0.2)',
			'rgba(255, 159, 64, 0.2)',
			'rgba(255, 205, 86, 0.2)',
			'rgba(75, 192, 192, 0.2)',
			'rgba(54, 162, 235, 0.2)',
			'rgba(153, 102, 255, 0.2)',
		  ],
		  borderColor: [
			'rgb(255, 99, 132)',
			'rgb(255, 159, 64)',
			'rgb(255, 205, 86)',
			'rgb(75, 192, 192)',
			'rgb(54, 162, 235)',
			'rgb(153, 102, 255)',
		  ],
		  borderWidth: 1
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
			text: 'تصنيف المسجلين في المركز حسب نوع الإعاقة'
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
			'rgba(0, 255, 128, 0.6)',
			'rgba(153, 204, 255, 0.7)',
		  ],
		  hoverOffset: 4,
		  borderWidth: 1
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
			'rgba(0, 255, 128, 0.6)',
			'rgba(153, 204, 255, 0.7)',
		  ],
		  hoverOffset: 4,
		  borderWidth: 1
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