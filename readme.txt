current python 3.8

### INSTALL REQUIREMENTS ###
pip install fastapi uvicorn soundfile 
cd app/vietTTS
pip install -e .

### START SERVER ###
uvicorn wsgi:app --reload

### RUN DOCKER ###
docker pull nqcccccc/techres-viet-tts
docker run -p 8080:8080 nqcccccc/techres-viet-tts

### SAMPLE JQUERY ###
var settings = {
  "url": "localhost:8000/nude-detect",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "text":"Đó không phải là số cán bộ dôi dư, mà là số biên chế thực tế, cần thiết nhưng chưa có sự phê duyệt chính thức của Trung ương. Với khối lượng công việc ngày một tăng, công chức, viên chức, cán bộ không chuyên trách và người lao động làm việc tại thành phố hồ chí minh ngày càng bị áp lực. Không tính khách vãng lai, trung bình theo số biên chế được hội đồng nhân dân giao hiện nay, mỗi công chức phục vụ khoảng tám trăm bốn mươi tư người dân; nếu tính cả biên chế phường xã, mỗi công chức phục vụ ba trăm bốn mươi sáu người dân.",
    "silence":0.2,
    "sample_rate":16000
  }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});

PARAMS:
  - text: string - prenormalize shorten text, english, and numbers.
  - silence: float - the silence length between comma and dot.
  - sample_rate: int - audio rate (prefer 16k for this model)

### SAMPLE RESPONSE ###

{
    "status": 200,
    "path": "public/audio/clip_720a6946-24b9-4124-8cf4-c0d9545e8020.wav"
}

### ACCESS TO AUDIO ###
http://localhost:8080/public/audio/public/audio/clip_720a6946-24b9-4124-8cf4-c0d9545e8020.wav