/* Operating-gate rollout regression. Read-only, static, no model E2E.
Usage: node test_operating_gate_contract.cjs /path/to/General_research_GPT
*/
function gateRegression(F) {
 const A=F["AGENTS.md"],C=F["06_COLLABORATION_WORKFLOW.md"],P=F["02_RESEARCH_PIPELINE.md"],S=F["04_STATE_MANAGEMENT.md"],out=[];
 function all(s,x){return x.every(t=>s.includes(t))}
 function t(id,fn){try{if(!fn())throw Error("assertion false");out.push({id,result:"PASS"})}catch(e){out.push({id,result:"FAIL",error:String(e)})}}
 t("G01 output duty",()=>all(A,["매 사용자 대상 최종 응답","운영 제안"]));
 t("G02 exceptions",()=>all(A,["조사 밖 단발 답변"])&&all(C,["도구 실행 중 진행 알림","마지막 부분에 한 번만"]));
 t("G03 statuses",()=>all(C,["권장","보류","없음","해당 없음","미검토"]));
 t("G04 none vs missing",()=>all(C,["실제 평가 없이 사용할 수 없고","닫지 않는다"]));
 t("G05 receipt not proof",()=>all(C,["필드를 출력했다고 관문 검토를 수행한 것이 아니다"]));
 t("G06 no implicit authorization",()=>all(C,["사용자 무응답은 승인이 아니다","새 필수 W-ID"]));
 t("G07 no new hold",()=>all(C,["일률적 HOLD"])&&all(P,["관련 없는 작업을 일률적으로 차단하지 않는다"]));
 t("G08 first result",()=>all(P,["처음 사용자에게 보고하려는 응답","Stage 5까지 미룰 수 없다"]));
 t("G09 separate plan expansion",()=>all(C,["기존 W-ID 누락 검사와 별개"])&&all(P,["계획 밖 새 조사축 탐색"]));
 t("G10 no proposal cap",()=>all(C,["개수 제한 없이","실행 조합","현재 자료로 진행하는 대안"]));
 t("G11 A vs D",()=>all(P,["기존 필수 결함 A","미승인 신규 축 D","임의 착수하지 않는다"]));
 t("G12 each stage",()=>all(C,["Stage 0~0.5","Stage 0.7","Stage 1 수집","Stage 2 반례","Stage 3~4","Stage 5 종료","Stage 6 보고서","Stage 7 최종","Stage 8 전달"]));
 t("G13 no mirror",()=>all(S,["매 응답 mirror를 만들지 않는다"]));
 t("G14 unmet gate",()=>all(P,["필수 전환 관문을 미실시했다면","전환 완료·종료 가능 판정으로 건너뛰지 않되"]));
 t("G15 version split",()=>all(A,["운영 규칙은","main"])&&all(S,["주입된 규칙 SHA"]));
 function guard(f){return all(f["AGENTS.md"],["매 사용자 대상 최종 응답"])&&all(f["06_COLLABORATION_WORKFLOW.md"],["미검토","일률적 HOLD"])&&all(f["02_RESEARCH_PIPELINE.md"],["계획 밖 새 조사축 탐색"])&&all(f["04_STATE_MANAGEMENT.md"],["매 응답 mirror를 만들지 않는다"])}
 t("N00 unmodified baseline",()=>guard(F));
 [["N01","AGENTS.md","매 사용자 대상 최종 응답"],["N02","06_COLLABORATION_WORKFLOW.md","미검토"],["N03","02_RESEARCH_PIPELINE.md","계획 밖 새 조사축 탐색"],["N04","06_COLLABORATION_WORKFLOW.md","일률적 HOLD"],["N05","04_STATE_MANAGEMENT.md","매 응답 mirror를 만들지 않는다"]].forEach(([id,path,needle])=>t(id+" detects loss",()=>{let modified=Object.assign({},F);modified[path]=modified[path].split(needle).join("");return !guard(modified)}));
 return {passed:out.filter(z=>z.result==="PASS").length,failed:out.filter(z=>z.result==="FAIL").length,results:out,grade:"STATIC_ONLY"};
}
if(typeof module!=="undefined"&&typeof require!=="undefined"&&require.main===module){
 const fs=require("node:fs"),path=require("node:path"),root=path.resolve(process.argv[2]||".");
 const names=["AGENTS.md","06_COLLABORATION_WORKFLOW.md","02_RESEARCH_PIPELINE.md","04_STATE_MANAGEMENT.md"];
 const f=Object.fromEntries(names.map(n=>[n,fs.readFileSync(path.join(root,n),"utf8")]));
 const result=gateRegression(f);console.log(JSON.stringify(result,null,2));process.exitCode=result.failed?1:0;
}
