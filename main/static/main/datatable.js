$(document).ready(function() {
  var oTable = $('.datatable').dataTable({
    "searching": true,
    "processing": true,
    "serverSide": true,
    "ajax": "{% url 'order_list_json' %}"
  });
});
