$( function(){

	$('div.main_menu_button#new_expense_main').click( function(){
		$('div.content').fadeOut('fast', function(){
			window.location.assign('/new_expense')
		});
	});

	$('div.main_menu_button#view_all_main').click( function(){
		$('div.content').fadeOut('fast', function(){
			window.location.assign('/all_transactions')
		});
	});

	$('div.main_menu_button#weekly_report_main').click( function(){
		$('div.content').fadeOut('fast', function(){
			window.location.assign('/weekly_report')
		});
	});

});