var ctx = document.getElementById("c").getContext("2d");

var donut = new Chart(ctx).Doughnut(
	// Datas
	[
		{
			value: 100,
			color:"#F7464A",
			highlight: "#FF5A5E",
			label: "Red"
		},
		{
			value: 100,
			color: "#46BFBD",
			highlight: "#5AD3D1",
			label: "Green"
		},
	],
	// Options
	{
		segmentShowStroke : true,
		segmentStrokeColor : "#fff",
		segmentStrokeWidth : 2,
		percentageInnerCutout : 50,
		animationSteps : 50,
		animationEasing : "easeOutBounce",
		animateRotate : true,
		animateScale : false,
		responsive: true,
		showScale: true,
        animateScale: true,
        maintainAspectRatio : false
	});