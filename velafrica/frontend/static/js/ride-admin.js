function check_address(obj, fieldset) {
    if (obj.children(":selected") && obj.children(":selected").val()) {
        fieldset.css("display", "none");
    } else {
        fieldset.css("display", "block");
    }
}

function check_from_address() {
    check_address(django.jQuery('select#id_from_warehouse'), django.jQuery('fieldset.from_address'))
}

function check_to_address() {
    check_address(django.jQuery('select#id_to_warehouse'), django.jQuery('fieldset.to_address'))
}

function invoice_address_fieldset() {
    if (!!django.jQuery("#id_invoice_same_as_customer") && !django.jQuery("#id_invoice_same_as_customer").is(':checked')) {
        if (django.jQuery('fieldset.invoice_address').css('display') == 'none' && django.jQuery('fieldset.invoice_address').hasClass("collapsed")) {
            django.jQuery('fieldset.invoice_address .collapse-toggle').click()
        }
        django.jQuery('fieldset.invoice_address').css('display', 'block');
    } else {
        django.jQuery('fieldset.invoice_address').css('display', 'none');
    }
}


function invoice_fieldset() {
    if (django.jQuery("#id_charged").is(':checked')) {
        if (django.jQuery('fieldset.invoice').css('display') == 'none' && django.jQuery('fieldset.invoice').hasClass("collapsed")) {
            django.jQuery('fieldset.invoice .collapse-toggle').click()
        }
        django.jQuery('fieldset.invoice').css('display', 'block');
        django.jQuery("#id_invoice_same_as_customer").change(invoice_address_fieldset);

    } else {
        django.jQuery('fieldset.invoice').css('display', 'none');
        django.jQuery('fieldset.invoice_address').css('display', 'none');
    }
}

django.jQuery(function () {
    check_from_address();
    check_to_address();
    invoice_fieldset();
    //invoice_address_fieldset();
    django.jQuery('select#id_from_warehouse').change(check_from_address);
    django.jQuery('select#id_to_warehouse').change(check_to_address);
    django.jQuery("#id_charged").change(invoice_fieldset);
    django.jQuery("#id_invoice_same_as_customer").change(invoice_address_fieldset);
});
