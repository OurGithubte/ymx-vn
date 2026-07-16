"use client";

import { FormEvent, useState } from "react";
import { CheckCircle2, LoaderCircle, UploadCloud } from "lucide-react";

const formCopy={
  vi:{name:"Họ và tên",email:"Email",phone:"Điện thoại",experience:"Số năm kinh nghiệm",intro:"Giới thiệu ngắn",upload:"Tải CV của bạn",fileHint:"PDF hoặc DOCX, tối đa 5 MB",consent:"Tôi đồng ý để YMX xử lý thông tin cho mục đích tuyển dụng theo",privacy:"thông báo quyền riêng tư ứng viên",submit:"Gửi hồ sơ",sending:"Đang gửi…",success:"Đã nhận hồ sơ",successText:"Cảm ơn bạn. Bộ phận tuyển dụng sẽ xem xét và liên hệ qua email.",fallback:"Không thể gửi hồ sơ."},
  en:{name:"Full name",email:"Email",phone:"Phone",experience:"Years of experience",intro:"Short introduction",upload:"Upload your CV",fileHint:"PDF or DOCX, maximum 5 MB",consent:"I consent to YMX processing my information for recruitment purposes under the",privacy:"candidate privacy notice",submit:"Submit application",sending:"Submitting…",success:"Application received",successText:"Thank you. Our recruitment team will review your profile and contact you by email.",fallback:"Unable to submit application."},
  zh:{name:"姓名",email:"电子邮箱",phone:"联系电话",experience:"工作年限",intro:"简短介绍",upload:"上传简历",fileHint:"PDF或DOCX，最大5 MB",consent:"我同意YMX根据",privacy:"应聘者隐私声明",submit:"提交申请",sending:"正在提交…",success:"申请已收到",successText:"感谢您的申请。招聘团队将审核您的资料并通过电子邮件联系您。",fallback:"暂时无法提交申请。"},
} as const;

export function ApplicationForm({jobId,locale}:{jobId:string;locale:string}){
  const lang=locale==="zh"?"zh":locale==="en"?"en":"vi";const c=formCopy[lang];
  const [state,setState]=useState<"idle"|"sending"|"success"|"error">("idle");const [message,setMessage]=useState("");
  async function submit(event:FormEvent<HTMLFormElement>){event.preventDefault();setState("sending");setMessage("");const data=new FormData(event.currentTarget);data.set("jobId",jobId);data.set("locale",lang);try{const response=await fetch("/api/applications",{method:"POST",body:data});const result=await response.json();if(!response.ok)throw new Error(result.error||c.fallback);setState("success");event.currentTarget.reset()}catch(error){setState("error");setMessage(error instanceof Error?error.message:c.fallback)}}
  if(state==="success")return <div className="success-box"><CheckCircle2/><h2>{c.success}</h2><p>{c.successText}</p></div>;
  return <form className="application-form" onSubmit={submit}>
    <label className="form-trap" aria-hidden="true">Website<input name="website" tabIndex={-1} autoComplete="off"/></label>
    <div className="form-grid"><label>{c.name}<input name="fullName" required minLength={2}/></label><label>{c.email}<input name="email" type="email" required/></label><label>{c.phone}<input name="phone" type="tel" required/></label><label>{c.experience}<input name="experienceYears" type="number" min="0" max="50"/></label></div>
    <label>{c.intro}<textarea name="coverNote" rows={5} maxLength={2000}/></label>
    <label className="upload-field"><UploadCloud/><span><strong>{c.upload}</strong><small>{c.fileHint}</small></span><input name="cv" type="file" accept=".pdf,.doc,.docx,application/pdf" required/></label>
    <label className="consent"><input name="consent" type="checkbox" required/><span>{c.consent} <a href={`/${lang}/privacy`} target="_blank">{c.privacy}</a>.</span></label>
    {state==="error"&&<p className="form-error">{message}</p>}<button className="button primary submit" disabled={state==="sending"}>{state==="sending"?<><LoaderCircle className="spin"/>{c.sending}</>:c.submit}</button>
  </form>;
}
