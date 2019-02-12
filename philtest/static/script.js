$('#login').click(function() {
	$('#dark').show();
	$('#loginblock').show();
});
$('#quote-add-p').click(function() {
	if ($('#addform').css("display") == "none") {
		$('#addform').show();
	} else {
		$('#addform').hide();
	}
});
$('#dark').click(function() {
	$(this).hide();
	$('#loginblock').hide();
});
$('#search').on("input", function() {
	$('#quote-add').hide();
	var poisk = $(this).val().toLowerCase();
	if (poisk.length > 0) {
		$('.quote-block').each(function() {
			var quote = $(this);
			quote.find('span').each(function() {
				var name = $(this).text();
				var i = name.toLowerCase().indexOf(poisk);
				if (i + 1) {
					var up = name.substr(i, poisk.length);
					var span = '<span style="background: #ffff00;">' + up + '</span>';
					var rename = name.replace(up, span);
					$(this).html(rename);
					quote.show();
					return false;
				} else {
					$(this).find('span').each(function() {						
						$(this).css('background', 'rgba(0,0,0,0)');
					})
					quote.hide();
				}
			});
		});
	} else {
		$('.quote-block').each(function() {
			var quote = $(this);
			quote.find('span').each(function() {
				$(this).css('background', 'rgba(0,0,0,0)');
			});
			$(this).show();
			$('#quote-add').show();
		});
	}
});