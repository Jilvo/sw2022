function generate() {
    var email = $('#email').val();
    var subject = $('#subject').val();
    var body = $('#message').val();
  
    var mailto = 'mailto:' + email;
    var params = {};
    if (subject) {
      params.subject = subject;
    }
    if (body) {
      params.body = body;
    }
    if (params) {
      mailto += '?' + $.param(params);
    }
  
    var $output = $('#output');
    $output.val(mailto);
    $output.focus();
    $output.select();
    document.execCommand('copy');
  }
  
  $(document).ready(function() {
    $('#send').on('click', generate);
    console.log(generate)
  });