
function APlusFieldset() {
    if(django.jQuery("#id_a_plus").is(':checked')) {
        if (django.jQuery('fieldset.a_plus_fieldset').css('display') == 'none' && django.jQuery('fieldset.a_plus_fieldset').hasClass("collapsed")) {
           django.jQuery('fieldset.a_plus_fieldset .collapse-toggle').click()
        }
        django.jQuery('fieldset.a_plus_fieldset').css('display', 'block');
    }
    else {
        django.jQuery('fieldset.a_plus_fieldset').css('display', 'none');
    }

}

django.jQuery(function () {
    APlusFieldset()
    django.jQuery('#id_a_plus').change(APlusFieldset);
})