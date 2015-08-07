// $(function() {
//     $('#btnSignUp').click(function() {
 
//         $.ajax({
//             url: '/signup',
//             data: $('form').serialize(),
//             type: 'POST',
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });

function check() {
  document.getElementById('other-amount').readOnly = !document.getElementById('amount-5').checked;
}
