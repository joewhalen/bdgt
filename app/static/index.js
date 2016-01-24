$( function(){

	$('div.main_menu_button#new_expense_main').click( function(){
		$('div#main_menu').fadeOut('fast', function(){
			window.location.replace('/new_expense')
		});
	});

	$('div.main_menu_button#view_all_main').click( function(){
		$('div#main_menu').fadeOut('fast', function(){
			window.location.replace('/all_transactions')
		});
	});

	$('div.main_menu_button#weekly_report_main').click( function(){
		$('div#main_menu').fadeOut('fast', function(){
			window.location.replace('/weekly_report')
		});
	});

});