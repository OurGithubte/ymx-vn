import type { Locale } from "./i18n";

export type CandidateEmailType="interview"|"rejected"|"offered";
export function escapeHtml(value:string){return value.replace(/[&<>'"]/g,char=>({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[char]||char))}
export function safeSubject(value:string){return value.replace(/[\r\n]/g," ").trim()}

export function applicationReceived(locale:Locale,name:string,job:string){
  const n=escapeHtml(name),j=escapeHtml(job),subjectJob=safeSubject(job);
  if(locale==="vi")return {subject:`YMX đã nhận hồ sơ ứng tuyển – ${subjectJob}`,html:`<p>Xin chào ${n},</p><p>Cảm ơn bạn đã ứng tuyển vị trí <strong>${j}</strong>. Bộ phận tuyển dụng YMX đã nhận hồ sơ và sẽ liên hệ qua email nếu hồ sơ phù hợp.</p><p>Phòng Tuyển dụng YMX Việt Nam</p>`};
  if(locale==="zh")return {subject:`YMX已收到您的应聘申请 – ${subjectJob}`,html:`<p>${n}，您好！</p><p>感谢您申请<strong>${j}</strong>职位。YMX招聘团队已收到您的资料，如进入下一阶段，我们将通过电子邮件与您联系。</p><p>越南YMX招聘团队</p>`};
  return {subject:`YMX has received your application – ${subjectJob}`,html:`<p>Dear ${n},</p><p>Thank you for applying for <strong>${j}</strong>. Our recruitment team has received your application and will contact you by email if your profile is shortlisted.</p><p>YMX Vietnam Recruitment</p>`};
}

export function candidateStatusEmail(input:{locale:Locale;type:CandidateEmailType;name:string;job:string;interviewAt?:string;location?:string;note?:string}){
  const n=escapeHtml(input.name),j=escapeHtml(input.job),subjectJob=safeSubject(input.job);
  const interviewDate=input.interviewAt?new Date(/[zZ]|[+-]\d\d:\d\d$/.test(input.interviewAt)?input.interviewAt:`${input.interviewAt}${input.interviewAt.length===16?":00":""}+07:00`):null;
  const time=interviewDate?interviewDate.toLocaleString(input.locale==="vi"?"vi-VN":input.locale==="zh"?"zh-CN":"en-GB",{timeZone:"Asia/Ho_Chi_Minh"}):"";
  const location=input.location?escapeHtml(input.location):"";const note=input.note?`<p>${escapeHtml(input.note).replace(/\n/g,"<br>")}</p>`:"";
  if(input.locale==="vi"){
    if(input.type==="interview")return {subject:`Thư mời phỏng vấn – ${subjectJob}`,html:`<p>Xin chào ${n},</p><p>YMX Việt Nam trân trọng mời bạn tham dự phỏng vấn cho vị trí <strong>${j}</strong>.</p>${time?`<p><strong>Thời gian:</strong> ${time}</p>`:""}${location?`<p><strong>Địa điểm:</strong> ${location}</p>`:""}${note}<p>Phòng Tuyển dụng YMX Việt Nam</p>`};
    if(input.type==="offered")return {subject:`Kết quả ứng tuyển – ${subjectJob}`,html:`<p>Xin chào ${n},</p><p>Chúng tôi vui mừng thông báo bạn đã đạt kết quả cho vị trí <strong>${j}</strong>. Bộ phận tuyển dụng sẽ liên hệ về các bước tiếp theo.</p>${note}<p>Phòng Tuyển dụng YMX Việt Nam</p>`};
    return {subject:`Cập nhật hồ sơ ứng tuyển – ${subjectJob}`,html:`<p>Xin chào ${n},</p><p>Cảm ơn bạn đã dành thời gian ứng tuyển vị trí <strong>${j}</strong>. Sau khi cân nhắc, chúng tôi chưa thể tiếp tục hồ sơ của bạn trong đợt này. YMX trân trọng sự quan tâm của bạn.</p>${note}<p>Phòng Tuyển dụng YMX Việt Nam</p>`};
  }
  if(input.locale==="zh"){
    if(input.type==="interview")return {subject:`面试邀请 – ${subjectJob}`,html:`<p>${n}，您好！</p><p>越南YMX诚邀您参加<strong>${j}</strong>职位的面试。</p>${time?`<p><strong>时间：</strong>${time}</p>`:""}${location?`<p><strong>地点：</strong>${location}</p>`:""}${note}<p>越南YMX招聘团队</p>`};
    if(input.type==="offered")return {subject:`应聘结果 – ${subjectJob}`,html:`<p>${n}，您好！</p><p>很高兴通知您，您已通过<strong>${j}</strong>职位的招聘评估。招聘团队将联系您说明后续安排。</p>${note}<p>越南YMX招聘团队</p>`};
    return {subject:`应聘进度更新 – ${subjectJob}`,html:`<p>${n}，您好！</p><p>感谢您申请<strong>${j}</strong>职位。经慎重考虑，本次我们暂时无法继续推进您的申请。感谢您对越南YMX的关注。</p>${note}<p>越南YMX招聘团队</p>`};
  }
  if(input.type==="interview")return {subject:`Interview invitation – ${subjectJob}`,html:`<p>Dear ${n},</p><p>YMX Vietnam would like to invite you to an interview for <strong>${j}</strong>.</p>${time?`<p><strong>Time:</strong> ${time}</p>`:""}${location?`<p><strong>Location:</strong> ${location}</p>`:""}${note}<p>YMX Vietnam Recruitment</p>`};
  if(input.type==="offered")return {subject:`Application result – ${subjectJob}`,html:`<p>Dear ${n},</p><p>We are pleased to inform you that your application for <strong>${j}</strong> has been successful. Our recruitment team will contact you with the next steps.</p>${note}<p>YMX Vietnam Recruitment</p>`};
  return {subject:`Application update – ${subjectJob}`,html:`<p>Dear ${n},</p><p>Thank you for applying for <strong>${j}</strong>. After careful consideration, we will not be progressing your application at this time. We appreciate your interest in YMX Vietnam.</p>${note}<p>YMX Vietnam Recruitment</p>`};
}
