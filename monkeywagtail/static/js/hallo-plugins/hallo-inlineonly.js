(function() {
    (function($) {
        return $.widget('IKS.inlineonly', {
            options: {
                uuid: '',
                editable: null,
                buttonCssClass: null
            },
            populateToolbar: function(toolbar) {
                var whitelist = [
                    'halloformat',
                    'hallowagtaillink',
                    'hallowagtaildoclink',
                    'hallolists'
					// 'halloheadings',
        			// 'hallohr',
			        // 'halloreundo',
			        // 'hallorequireparagraphs',
                ];
                $(toolbar).children().filter(function() {
                    var className = this.className.split(/\s+/)[0];
                    return $.inArray(className, whitelist) == -1;
                }).remove();
            }
        });
    })(jQuery);

}).call(this);