src_audio = 'https://bigsoundbank.com/UPLOAD/mp3/0451.mp3?v=d'
var app = new Vue({
        el: '#app',
        data: {
            info: 'Just an object',
            dataStat: null,
            categories: [{name:'Лол', value:'Лол'}],
            selected: 'Все',
            preData: null,
            warData: null,
            lastData: null,
            len_warning: null,
        },
        created(){
            const socket = new WebSocket(`ws://${window.location.host}/ws/main_table/`);
            let _this = this;
            this.lastData = []
            socket.onmessage = function(event){
                // _this.dataStat = JSON.parse(event.data);

                if (_this.selected === 'Все'){
                    _this.warData = []
                    _this.dataStat = JSON.parse(event.data);
                    _this.preData = _this.dataStat;
                    for (let i = 0; i < _this.preData.length; i++) {
                        if (_this.preData[i].status === "тревога") {
                            _this.warData.push(_this.preData[i]);
                            if (_this.lastData.length < _this.warData.length) {
                                var audio = new Audio(src_audio)
                                audio.play();
                            }
                        }
                    }
                } else {
                    _this.dataStat = []
                    _this.warData = []
                    _this.preData = JSON.parse(event.data);
                    for (let i = 0; i < _this.preData.length; i++) {
                        if (_this.preData[i].category === _this.selected) {
                            _this.dataStat.push(_this.preData[i]);
                        }
                        if (_this.preData[i].status === 'тревога') {
                            _this.warData.push(_this.preData[i]);
                            if (_this.lastData.length < _this.warData.length) {
                                var audio = new Audio(src_audio)
                                audio.play();
                            }
                        }
                    }
                }
                _this.lastData = _this.warData;
                if (_this.warData.length > 0) {
                    _this.len_warning = _this.warData.length;
                } else {
                    _this.len_warning = null;
                }

            }
        },
        mounted() {
            axios
                .get('http://127.0.0.1:8000/web/categories/')
                .then(response => this.categories = response.data);
        }
    })