$(document).ready( function(){


	var kwargs = {displaylogo : false, displayModeBar : false};

	var linedata = []
	var bardata = []
	$.getJSON('/get_weekly_report', { type : 'bar' }).done( function(data){

		var barstyle = {
    		margin : { t : 10, r : 0, b : 40, l : 30 },
    		legend : { x : 0, y : 1},
    		paper_bgcolor : $('body').css('background-color'),
    		plot_bgcolor : $('body').css('background-color'),
    		font : { color : $('body').css('color')},
    		yaxis : { tickprefix : '$'}
		};

		if (data != { x : [], y : [] }){
			data['type']='bar';
			data['orientation'] = 'v';
			data['marker'] = { color : '#14cfa4'}
			bardata = [data]
			Plotly.newPlot('barPlot', [data], barstyle, kwargs)
		}
	});

	$.getJSON('/get_weekly_report', { type : 'line' }).done( function(data){
		
		if (data != { x : [], y : []}) {

			var lineps = {
	    		margin : { t : 10, r : 0, b : 40, l : 30 },
	    		legend : { x : 0, y : 1},
	    		paper_bgcolor : $('body').css('background-color'),
	    		plot_bgcolor : $('body').css('background-color'),
	    		font : { color : $('body').css('color')},
	    		yaxis : { tickprefix : '$'},
	    		xaxis : { type : 'date', dtick : 86400000},
	    		hoverinfo : 'text',
	    	};


			plotdata = [{ x : data['x'], y : data['y'], text : data['names'] }];
			plotdata[0]['line'] = { color : '#14cfa4'}


			Plotly.newPlot('linePlot', plotdata, lineps, kwargs);

			console.log(plotstyle)
		}
	});


});