function getParameterByName(name) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var url = window.location.href;
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return '';
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

$(document).ready(function () {
    $.ajax({
        url: './genarator/contrubute.json',
        type: 'GET',
        success: function (data) {
            var contributors = data;

            // Sắp xếp theo số lượng đề thi giảm dần
            contributors = Object.keys(contributors).sort(function (a, b) {
                return contributors[b] - contributors[a];
            }).reduce(function (result, key) {
                result[key] = contributors[key];
                return result;
            }, {});

            var html = '';
            for (key in contributors) {
                // html += "<span class='badge badge-dark' title='" + key + "\nĐã đóng góp " + contributors[key] + " đề thi'>" + key + "</span> ";
                // html += "&nbsp;";
                // badge notification
                html += "<span class='badge badge-dark' title='" + key + "\nĐã đóng góp " + contributors[key] + " đề thi'>" + key + " <span class='notification'>" + contributors[key] + "</span></span> ";
            }
            $('#contributors').html(html);
        }
    });
});


$(document).ready(function () {
    var table = $('#example').DataTable({
        search: {
            search: getParameterByName('s')
        },
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.21/i18n/Vietnamese.json"
        },
        "ajax": {
            "url": "./genarator/data.json",
            "dataSrc": function (json) {
                // Giả định json là mảng chứa dữ liệu
                return json;
            }
        },
        "columns": [
            { "data": "tinh" },
            { "data": "lop" },
            { "data": "nam" },
            { "data": "link" },
            { "data": "email" },
            { "data": null } // Cột này sẽ được custom
        ],
        // Định dạng cột link và checkbox
        "columnDefs": [
            {
                "targets": 1,
                "className": "text-center"

            },
            {
                "targets": 2,
                "className": "text-center"
            },
            {
                "targets": 3,
                "className": "text-center",
                "render": function (data, type, row, meta) {
                    return '<a href="https://github.com/zukahai/provincial-informatics-exam-questions/blob/main/' + row['file'] + '" target="_blank">Xem</a>';
                }
            },
            {
                "targets": 5,
                "orderable": false, // Không sắp xếp cột này
                "searchable": false, // Không tìm kiếm cột này
                "className": "text-center", // Căn giữa nội dung
                "render": function (data, type, row, meta) {
                    var isChecked = getLocalStorage(row['file']) == 1 ? 'checked' : '';
                    return '<input type="checkbox" name="tinh" value="' + getLocalStorage(row['tinh']) + '" onclick="abc(\'' + row['file'] + '\')" ' + isChecked + '>';
                }
            }
        ]
    });

    // Lọc dữ liệu dựa trên trạng thái checkbox
    $('#filterChecked, #filterUnchecked').on('change', function () {
        if (this.id === 'filterChecked') {
            $('#filterUnchecked').prop('checked', false);
        } else {
            $('#filterChecked').prop('checked', false);
        }
        table.draw();
    });

    $.fn.dataTable.ext.search.push(
        function (settings, data, dataIndex) {
            var showChecked = $('#filterChecked').is(':checked');
            var showUnchecked = $('#filterUnchecked').is(':checked');
            var file = table.row(dataIndex).data()['file'];
            var isChecked = getLocalStorage(file) == 1;

            if (showChecked && isChecked) {
                return true;
            }
            if (showUnchecked && !isChecked) {
                return true;
            }
            if (!showChecked && !showUnchecked) {
                return true;
            }
            return false;
        }
    );
});

function abc(id) {
    let data = localStorage.getItem(id);
    localStorage.setItem(id, 1 - data);
}

function getLocalStorage(id) {
    var data = localStorage.getItem(id);
    if (data)
        return data;
    localStorage.setItem(id, 0);
    return 0;
}