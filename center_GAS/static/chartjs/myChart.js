
Chart.defaults.font.size = 14;

function displayGenre(men, womans) {
	var genre = document.getElementById("genre").getContext("2d");
	const data = {
		labels: [
		  'ذكور',
		  'إناث',
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
				text: 'عدد الذكور و الإناث المسجلين في المركز'
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
		  //   label: 'My First Dataset',
			data: [child, young, old],
			backgroundColor: [
			  'rgba(255, 99, 132, 0.2)',
			  'rgba(255, 159, 64, 0.2)',
			  'rgba(255, 205, 86, 0.2)',
			],
			borderColor: [
			  'rgb(255, 99, 132)',
			  'rgb(255, 159, 64)',
			  'rgb(255, 205, 86)',
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
				text: 'طلبات الإستفادة من بطاقة شخص في وضعية إعاقة'
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
				text: ' طلبات الإستفادة من الطرد الغدائي'
			  }
			}
		  },
	  };
	var genrePie = new Chart(food,config);
}


function displayDevice(ele, hasHelpDevice, waitingHelpDevice, message) {
	var ele = document.getElementById(ele).getContext("2d");
	const data = {
		labels: [
		  'مستفيدون',
		  'لائحة الإنتضار',
		],
		datasets: [{
		  data: [hasHelpDevice, waitingHelpDevice],
		  backgroundColor: [
			'rgba(0, 255, 128, 0.6)',
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
				text: message
			  }
			}
		  },
	  };
	var genrePie = new Chart(ele,config);
}


function displayProjects(local, regional, central, finish) {
	var projects = document.getElementById("projects").getContext("2d");
	
	var mybarChart = new Chart(projects, {
	  type: 'bar',
	  data: {
		labels: ['قيد الدراسة الإقليمية' , 'قيد الدراسة الجهوية', 'قيد الدراسة المركزية', 'مشاريع ممولة'],
		datasets: [{
		//   label: 'My First Dataset',
		  data: [local, regional, central, finish],
		  backgroundColor: [
			'rgba(255, 99, 132, 0.2)',
			'rgba(255, 159, 64, 0.2)',
			'rgba(255, 205, 86, 0.2)',
			'rgba(75, 192, 192, 0.2)',
		  ],
		  borderColor: [
			'rgb(255, 99, 132)',
			'rgb(255, 159, 64)',
			'rgb(255, 205, 86)',
			'rgb(75, 192, 192)',
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
			text: 'عرض المشاريع حسب حالة الطلب'
		  }
		}
	  },
	});
}