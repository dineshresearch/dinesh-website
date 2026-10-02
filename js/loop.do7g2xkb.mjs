import{t as e}from"./rolldown-runtime.dh6celcd.mjs";import{A as t,B as n,N as r,O as i,P as a,R as o,S as s,_ as c,j as l,l as u,s as d,u as f,w as p,y as m}from"./react.73opg4pm.mjs";import{I as h,N as g,S as _,V as v,a as y,f as b,r as ee,t as x}from"./motion.cthkkq98.mjs";import{B as S,Ct as te,D as ne,J as C,M as w,O as re,T as ie,V as T,_t as ae,ct as oe,g as se,i as ce,k as E,lt as le,o as D,s as O,wt as ue}from"./framer.bss_3ky8.mjs";import{l as k,u as A}from"./shared-lib.dho8zggo.mjs";import{n as j,t as M}from"./svgcomponent.dcxvbinw.mjs";import{i as de,n as N,r as P,t as fe}from"./mffbjovla.8seepgwm.mjs";import{n as pe,t as F}from"./scrolltrigger.bi3riouq.mjs";function I(e){let{paperType:t=`lined`,lineColor:n=`#d0d0d0`,lineSpacing:r=24,lineWidth:i=1,opacity:a=.3,paperTexture:o=!0,textureStyle:s=`vintage`,textureIntensity:c=30,background:d=`#ffffff`,shadow:p=!1,noise:m=!1,noiseIntensity:h=25,border:g}=e,_=`paper-pattern-${t}-${Math.random().toString(36).substr(2,9)}`;`${Math.random().toString(36).substr(2,9)}`;let v=()=>{switch(t){case`lined`:return u(`defs`,{children:u(`pattern`,{id:_,x:`0`,y:`0`,width:`100%`,height:r,patternUnits:`userSpaceOnUse`,children:u(`line`,{x1:`0`,y1:r,x2:`100%`,y2:r,stroke:n,strokeWidth:i,opacity:a})})});case`grid`:return u(`defs`,{children:f(`pattern`,{id:_,x:`0`,y:`0`,width:r,height:r,patternUnits:`userSpaceOnUse`,children:[u(`line`,{x1:`0`,y1:r,x2:r,y2:r,stroke:n,strokeWidth:i,opacity:a}),u(`line`,{x1:r,y1:`0`,x2:r,y2:r,stroke:n,strokeWidth:i,opacity:a})]})});case`dotted`:return u(`defs`,{children:u(`pattern`,{id:_,x:`0`,y:`0`,width:r,height:r,patternUnits:`userSpaceOnUse`,children:u(`circle`,{cx:r/2,cy:r/2,r:i,fill:n,opacity:a})})});case`wavy`:return u(`defs`,{children:u(`pattern`,{id:_,x:`0`,y:`0`,width:`100`,height:r,patternUnits:`userSpaceOnUse`,children:u(`path`,{d:`M 0,${r/2} Q 25,${r/2-8} 50,${r/2} T 100,${r/2}`,fill:`none`,stroke:n,strokeWidth:i,opacity:a})})});default:return null}},y=l(()=>{if(!o)return{};let e=c/100;switch(s){case`vintage`:return{filter:`
                        contrast(${1+e*.4}) 
                        brightness(${1-e*.2}) 
                        saturate(${1-e*.25})
                        sepia(${e*.35})
                        hue-rotate(${e*15}deg)
                    `,backgroundImage:`
                        radial-gradient(ellipse at 20% 30%, rgba(139, 69, 19, ${e*.25}) 0%, transparent 60%),
                        radial-gradient(ellipse at 80% 70%, rgba(160, 82, 45, ${e*.22}) 0%, transparent 55%),
                        radial-gradient(ellipse at 40% 80%, rgba(210, 180, 140, ${e*.18}) 0%, transparent 45%),
                        radial-gradient(ellipse at 70% 20%, rgba(222, 184, 135, ${e*.2}) 0%, transparent 50%),
                        radial-gradient(ellipse at 10% 60%, rgba(205, 133, 63, ${e*.15}) 0%, transparent 40%),
                        linear-gradient(45deg, rgba(139, 69, 19, ${e*.08}) 0%, transparent 30%, rgba(160, 82, 45, ${e*.06}) 70%),
                        linear-gradient(-30deg, rgba(222, 184, 135, ${e*.1}) 0%, transparent 40%)
                    `};case`modern`:return{filter:`
                        contrast(${1+e*.15}) 
                        brightness(${1-e*.08})
                        saturate(${1+e*.1})
                    `,backgroundImage:`
                        linear-gradient(45deg, rgba(0, 0, 0, ${e*.04}) 25%, transparent 25%),
                        linear-gradient(-45deg, rgba(0, 0, 0, ${e*.04}) 25%, transparent 25%),
                        linear-gradient(45deg, transparent 75%, rgba(0, 0, 0, ${e*.04}) 75%),
                        linear-gradient(-45deg, transparent 75%, rgba(0, 0, 0, ${e*.04}) 75%),
                        radial-gradient(circle at 25% 25%, rgba(100, 100, 100, ${e*.06}) 0%, transparent 50%),
                        radial-gradient(circle at 75% 75%, rgba(120, 120, 120, ${e*.05}) 0%, transparent 45%)
                    `,backgroundSize:`3px 3px, 3px 3px, 3px 3px, 3px 3px, 20px 20px, 25px 25px`,backgroundPosition:`0 0, 0 1.5px, 1.5px -1.5px, -1.5px 0px, 0 0, 10px 10px`};case`rough`:return{filter:`
                        contrast(${1+e*.6}) 
                        brightness(${1-e*.3})
                        blur(${e*.4}px)
                        saturate(${1-e*.2})
                    `,backgroundImage:`
                        radial-gradient(ellipse at 15% 85%, rgba(101, 67, 33, ${e*.3}) 0%, transparent 60%),
                        radial-gradient(ellipse at 85% 15%, rgba(139, 69, 19, ${e*.28}) 0%, transparent 65%),
                        radial-gradient(ellipse at 35% 45%, rgba(160, 82, 45, ${e*.25}) 0%, transparent 55%),
                        radial-gradient(ellipse at 65% 75%, rgba(205, 133, 63, ${e*.22}) 0%, transparent 50%),
                        radial-gradient(ellipse at 50% 20%, rgba(139, 69, 19, ${e*.2}) 0%, transparent 45%),
                        linear-gradient(30deg, rgba(101, 67, 33, ${e*.15}) 0%, transparent 40%, rgba(139, 69, 19, ${e*.12}) 80%),
                        linear-gradient(-60deg, rgba(160, 82, 45, ${e*.18}) 0%, transparent 35%)
                    `};case`smooth`:return{filter:`
                        contrast(${1+e*.08}) 
                        brightness(${1-e*.04})
                        saturate(${1+e*.05})
                    `,backgroundImage:`
                        linear-gradient(0deg, rgba(0, 0, 0, ${e*.02}) 50%, transparent 50%),
                        linear-gradient(90deg, rgba(0, 0, 0, ${e*.02}) 50%, transparent 50%),
                        radial-gradient(circle at 30% 30%, rgba(200, 200, 200, ${e*.04}) 0%, transparent 40%),
                        radial-gradient(circle at 70% 70%, rgba(220, 220, 220, ${e*.03}) 0%, transparent 35%)
                    `,backgroundSize:`1.5px 1.5px, 1.5px 1.5px, 15px 15px, 18px 18px`};default:return{}}},[o,s,c]);return f(`div`,{style:{width:`100%`,height:`100%`,position:`relative`,boxSizing:`border-box`,backgroundColor:d,boxShadow:p?`0 4px 12px rgba(0, 0, 0, 0.15)`:`none`,...y,...g,...e.style},children:[m&&u(`div`,{style:{position:`absolute`,top:0,left:0,width:`100%`,height:`100%`,opacity:h/100,pointerEvents:`none`,backgroundImage:`url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.4'/%3E%3C/svg%3E")`,mixBlendMode:`multiply`}}),o&&u(`div`,{style:{position:`absolute`,top:0,left:0,width:`100%`,height:`100%`,opacity:c/100*.8,backgroundImage:s===`vintage`?`
                            repeating-linear-gradient(
                                0deg,
                                transparent,
                                transparent 0.8px,
                                rgba(139, 69, 19, 0.12) 0.8px,
                                rgba(139, 69, 19, 0.12) 1.6px
                            ),
                            repeating-linear-gradient(
                                90deg,
                                transparent,
                                transparent 0.8px,
                                rgba(160, 82, 45, 0.1) 0.8px,
                                rgba(160, 82, 45, 0.1) 1.6px
                            ),
                            repeating-linear-gradient(
                                45deg,
                                transparent,
                                transparent 3px,
                                rgba(222, 184, 135, 0.08) 3px,
                                rgba(222, 184, 135, 0.08) 4px
                            )
                        `:s===`rough`?`
                            repeating-linear-gradient(
                                35deg,
                                transparent,
                                transparent 1.5px,
                                rgba(101, 67, 33, 0.15) 1.5px,
                                rgba(101, 67, 33, 0.15) 2.5px
                            ),
                            repeating-linear-gradient(
                                -55deg,
                                transparent,
                                transparent 2px,
                                rgba(139, 69, 19, 0.12) 2px,
                                rgba(139, 69, 19, 0.12) 3px
                            ),
                            repeating-linear-gradient(
                                80deg,
                                transparent,
                                transparent 4px,
                                rgba(160, 82, 45, 0.1) 4px,
                                rgba(160, 82, 45, 0.1) 5px
                            )
                        `:s===`modern`?`
                            repeating-linear-gradient(
                                0deg,
                                transparent,
                                transparent 0.5px,
                                rgba(0, 0, 0, 0.08) 0.5px,
                                rgba(0, 0, 0, 0.08) 1px
                            ),
                            repeating-linear-gradient(
                                90deg,
                                transparent,
                                transparent 0.5px,
                                rgba(0, 0, 0, 0.06) 0.5px,
                                rgba(0, 0, 0, 0.06) 1px
                            )
                        `:`
                            repeating-linear-gradient(
                                0deg,
                                transparent,
                                transparent 0.7px,
                                rgba(0, 0, 0, 0.06) 0.7px,
                                rgba(0, 0, 0, 0.06) 1.4px
                            ),
                            repeating-linear-gradient(
                                90deg,
                                transparent,
                                transparent 0.7px,
                                rgba(0, 0, 0, 0.04) 0.7px,
                                rgba(0, 0, 0, 0.04) 1.4px
                            )
                        `,pointerEvents:`none`,mixBlendMode:s===`vintage`?`multiply`:`normal`}}),o&&c>40&&u(`div`,{style:{position:`absolute`,top:0,left:0,width:`100%`,height:`100%`,opacity:(c-40)/100*.6,backgroundImage:s===`vintage`?`
                            radial-gradient(circle at 10% 10%, rgba(139, 69, 19, 0.15) 0%, transparent 30%),
                            radial-gradient(circle at 90% 90%, rgba(160, 82, 45, 0.12) 0%, transparent 25%),
                            radial-gradient(circle at 30% 70%, rgba(205, 133, 63, 0.1) 0%, transparent 35%),
                            radial-gradient(circle at 70% 30%, rgba(222, 184, 135, 0.08) 0%, transparent 40%)
                        `:s===`rough`?`
                            radial-gradient(circle at 20% 20%, rgba(101, 67, 33, 0.2) 0%, transparent 40%),
                            radial-gradient(circle at 80% 80%, rgba(139, 69, 19, 0.18) 0%, transparent 35%),
                            radial-gradient(circle at 50% 10%, rgba(160, 82, 45, 0.15) 0%, transparent 30%)
                        `:`
                            radial-gradient(circle at 25% 25%, rgba(0, 0, 0, 0.05) 0%, transparent 50%),
                            radial-gradient(circle at 75% 75%, rgba(0, 0, 0, 0.03) 0%, transparent 45%)
                        `,pointerEvents:`none`,mixBlendMode:`overlay`}}),f(`svg`,{width:`100%`,height:`100%`,style:{position:`absolute`,top:0,left:0,width:`100%`,height:`100%`},children:[v(),t!==`blank`&&u(`rect`,{width:`100%`,height:`100%`,fill:`url(#${_})`})]})]})}var me=e((()=>{d(),C(),p(),E(I,{background:{type:D.Color,title:`Background`,defaultValue:`#ffffff`},border:{type:D.Border,title:`Border`},shadow:{type:D.Boolean,title:`Shadow`,defaultValue:!1,enabledTitle:`On`,disabledTitle:`Off`},noise:{type:D.Boolean,title:`Noise`,defaultValue:!1,enabledTitle:`On`,disabledTitle:`Off`},noiseIntensity:{type:D.Number,title:`Noise Intensity`,defaultValue:25,min:5,max:60,step:5,unit:`%`,hidden:({noise:e})=>!e},paperType:{type:D.Enum,title:`Paper Type`,options:[`lined`,`grid`,`dotted`,`blank`,`wavy`],optionTitles:[`Lined`,`Grid`,`Dotted`,`Blank`,`Wavy`],defaultValue:`lined`,displaySegmentedControl:!0},lineColor:{type:D.Color,title:`Line Color`,defaultValue:`#d0d0d0`,hidden:({paperType:e})=>e===`blank`},lineSpacing:{type:D.Number,title:`Line Spacing`,defaultValue:24,min:8,max:120,step:2,unit:`px`,hidden:({paperType:e})=>e===`blank`},lineWidth:{type:D.Number,title:`Line Width`,defaultValue:1,min:.5,max:4,step:.5,unit:`px`,hidden:({paperType:e})=>e===`blank`},opacity:{type:D.Number,title:`Line Opacity`,defaultValue:.3,min:.1,max:1,step:.1,hidden:({paperType:e})=>e===`blank`},paperTexture:{type:D.Boolean,title:`Paper Texture`,defaultValue:!0,enabledTitle:`On`,disabledTitle:`Off`},textureStyle:{type:D.Enum,title:`Texture Style`,options:[`vintage`,`modern`,`rough`,`smooth`],optionTitles:[`Vintage`,`Modern`,`Rough`,`Smooth`],defaultValue:`vintage`,displaySegmentedControl:!0,hidden:({paperTexture:e})=>!e},textureIntensity:{type:D.Number,title:`Texture Intensity`,defaultValue:30,min:10,max:80,step:5,unit:`%`,hidden:({paperTexture:e})=>!e}})}));function L(e,...t){let n={};return t?.forEach(t=>t&&Object.assign(n,e[t])),n}var R,z,B,V,H,U,W,G,K,q,J,Y,he=e((()=>{d(),C(),x(),p(),j(),de(),R=S(M),z={f_D_QmORM:{hover:!0},ubuftqAhL:{hover:!0},ypBdqWJVj:{hover:!0}},B=[`ubuftqAhL`,`ypBdqWJVj`,`f_D_QmORM`],V=`framer-YVcpB`,H={f_D_QmORM:`framer-v-kxlijb`,ubuftqAhL:`framer-v-9o7ndm`,ypBdqWJVj:`framer-v-11ob9oj`},U={bounce:0,delay:0,duration:.4,type:`spring`},W=({value:e,children:n})=>{let r=t(y),i=e??r.transition,a=l(()=>({...r,transition:i}),[JSON.stringify(i)]);return u(y.Provider,{value:a,children:n})},G={"Dark Button":`ypBdqWJVj`,"White Button":`f_D_QmORM`,Default:`ubuftqAhL`},K=_.create(a),q=({click:e,height:t,id:n,link:r,showIcon:i,title:a,width:o,...s})=>({...s,cUOC4w3WT:e??s.cUOC4w3WT,errt8torn:a??s.errt8torn??`Contact`,OY8OQlhvY:i??s.OY8OQlhvY??!0,variant:G[s.variant]??s.variant??`ubuftqAhL`,zt8ifGc_Q:r??s.zt8ifGc_Q}),J=(e,t)=>e.layoutDependency?t.join(`-`)+e.layoutDependency:t.join(`-`),Y=ue(c(function(e,t){let n=i(null),r=t??n,o=m(),{activeLocale:s,setLocale:c}=ae();le();let{style:l,className:d,layoutId:p,variant:h,cUOC4w3WT:g,zt8ifGc_Q:v,errt8torn:y,OY8OQlhvY:b,...x}=q(e),{baseVariant:S,classNames:C,clearLoadingGesture:re,gestureHandlers:T,gestureVariant:E,isLoading:D,setGestureState:O,setVariant:ue,variants:k}=te({cycleOrder:B,defaultVariant:`ubuftqAhL`,enabledGestures:z,ref:r,variant:h,variantClassNames:H}),A=J(e,k),{activeVariantCallback:j,delay:de}=oe(S),N=j(async(...e)=>{if(O({isPressed:!1}),g&&await g(...e)===!1)return!1}),P=w(V,fe);return u(ee,{id:p??o,children:u(K,{animate:k,initial:!1,children:u(W,{value:U,children:u(se,{href:v,motionChild:!0,nodeId:`ubuftqAhL`,openInNewTab:!1,scopeId:`Zq7grirf4`,smoothScroll:!0,children:f(_.a,{...x,...T,className:`${w(P,`framer-9o7ndm`,d,C)} framer-11o3b02`,"data-border":!0,"data-framer-name":`Default`,"data-highlight":!0,layoutDependency:A,layoutId:`ubuftqAhL`,onTap:N,ref:r,style:{"--border-bottom-width":`1px`,"--border-color":`var(--token-4f4ed186-9023-4858-830a-5202d69249c1, rgb(17, 18, 18))`,"--border-left-width":`1px`,"--border-right-width":`1px`,"--border-style":`solid`,"--border-top-width":`1px`,backgroundColor:`rgba(0, 0, 0, 0)`,...l},variants:{"f_D_QmORM-hover":{backgroundColor:`rgba(0, 0, 0, 0)`},"ubuftqAhL-hover":{backgroundColor:`var(--token-4f4ed186-9023-4858-830a-5202d69249c1, rgb(17, 18, 18))`},"ypBdqWJVj-hover":{backgroundColor:`rgba(0, 0, 0, 0)`},f_D_QmORM:{"--border-color":`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`,"--border-left-width":`0px`,"--border-right-width":`0px`,"--border-top-width":`0px`},ypBdqWJVj:{"--border-left-width":`0px`,"--border-right-width":`0px`,"--border-top-width":`0px`}},...L({"f_D_QmORM-hover":{"data-framer-name":void 0},"ubuftqAhL-hover":{"data-framer-name":void 0},"ypBdqWJVj-hover":{"data-framer-name":void 0},f_D_QmORM:{"data-framer-name":`White Button`},ypBdqWJVj:{"data-framer-name":`Dark Button`}},S,E),children:[b!==!1&&u(ce,{children:u(ne,{className:`framer-ijnmpo-container`,"data-code-component-plugin-id":`84d4c1`,isAuthoredByUser:!0,layoutDependency:A,layoutId:`m1bXFVwNd-container`,nodeId:`m1bXFVwNd`,rendersWithMotion:!0,scopeId:`Zq7grirf4`,style:{rotate:0},variants:{"f_D_QmORM-hover":{rotate:0},"ubuftqAhL-hover":{rotate:0},"ypBdqWJVj-hover":{rotate:0},f_D_QmORM:{rotate:-45},ypBdqWJVj:{rotate:-45}},children:u(M,{color:`var(--token-4f4ed186-9023-4858-830a-5202d69249c1, rgb(17, 18, 18))`,height:`100%`,id:`m1bXFVwNd`,layoutId:`m1bXFVwNd`,stroke:!1,strokeColor:`var(--token-4f4ed186-9023-4858-830a-5202d69249c1, rgb(17, 18, 18))`,style:{height:`100%`,width:`100%`},svgCode:`<svg width="357" height="357" viewBox="0 0 357 357" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M141.973 85.5469C106.123 54.7091 52.0556 58.797 21.2493 94.6746C-9.51888 130.508 -5.43715 184.493 30.3689 215.293L176.234 340.762L177.378 342.095L177.581 341.921L177.783 342.095L178.928 340.762L324.793 215.293C360.599 184.493 364.681 130.508 333.912 94.6746C303.106 58.797 249.039 54.7091 213.188 85.5469L177.581 116.176L141.973 85.5469Z" fill="#F4ADB3"/>
</svg>
`,width:`100%`,...L({"ubuftqAhL-hover":{color:`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`},f_D_QmORM:{color:`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`,strokeColor:`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`,svgCode:`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3.99984 13.0001L3.99984 11.0001L15.9998 11.0001L10.4998 5.50008L11.9198 4.08008L19.8398 12.0001L11.9198 19.9201L10.4998 18.5001L15.9998 13.0001L3.99984 13.0001Z" fill="black"/>
</svg>
`},ypBdqWJVj:{svgCode:`<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3.99984 13.0001L3.99984 11.0001L15.9998 11.0001L10.4998 5.50008L11.9198 4.08008L19.8398 12.0001L11.9198 19.9201L10.4998 18.5001L15.9998 13.0001L3.99984 13.0001Z" fill="black"/>
</svg>
`}},S,E)})})}),u(ie,{__fromCanvasComponent:!0,children:u(a,{children:u(_.p,{className:`framer-styles-preset-27ku3y`,"data-styles-preset":`MffBJovlA`,dir:`auto`,children:`Contact`})}),className:`framer-ar7qgq`,fonts:[`Inter`],layoutDependency:A,layoutId:`Xpw_6LmHA`,style:{"--framer-link-text-color":`rgb(0, 153, 255)`,"--framer-link-text-decoration":`underline`},text:y,variants:{"ubuftqAhL-hover":{"--extracted-r6o4lv":`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`},f_D_QmORM:{"--extracted-r6o4lv":`var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255))`}},verticalAlignment:`top`,withExternalLayout:!0,...L({"ubuftqAhL-hover":{children:u(a,{children:u(_.p,{className:`framer-styles-preset-27ku3y`,"data-styles-preset":`MffBJovlA`,dir:`auto`,style:{"--framer-text-color":`var(--extracted-r6o4lv, var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255)))`},children:`Contact`})})},f_D_QmORM:{children:u(a,{children:u(_.p,{className:`framer-styles-preset-27ku3y`,"data-styles-preset":`MffBJovlA`,dir:`auto`,style:{"--framer-text-color":`var(--extracted-r6o4lv, var(--token-341b58e0-d728-43ce-a1dc-e77a522cab4f, rgb(255, 255, 255)))`},children:`Contact`})})}},S,E)})]})})})})})}),[`@supports (aspect-ratio: 1) { body { --framer-aspect-ratio-supported: auto; } }`,`.framer-YVcpB.framer-11o3b02, .framer-YVcpB .framer-11o3b02 { display: block; }`,`.framer-YVcpB.framer-9o7ndm { align-content: center; align-items: center; cursor: pointer; display: flex; flex-direction: row; flex-wrap: nowrap; gap: 8px; height: min-content; justify-content: flex-start; overflow: var(--overflow-clip-fallback, clip); padding: 8px 16px 8px 16px; position: relative; text-decoration: none; width: min-content; }`,`.framer-YVcpB .framer-ijnmpo-container { aspect-ratio: 1 / 1; flex: none; height: var(--framer-aspect-ratio-supported, 16px); position: relative; width: 16px; z-index: 1; }`,`.framer-YVcpB .framer-ar7qgq { flex: none; height: auto; position: relative; white-space: pre; width: auto; }`,`.framer-YVcpB.framer-v-11ob9oj.framer-9o7ndm, .framer-YVcpB.framer-v-kxlijb.framer-9o7ndm { padding: 8px 0px 8px 0px; }`,`.framer-YVcpB.framer-v-11ob9oj .framer-ijnmpo-container, .framer-YVcpB.framer-v-kxlijb .framer-ijnmpo-container { order: 1; }`,`.framer-YVcpB.framer-v-11ob9oj .framer-ar7qgq, .framer-YVcpB.framer-v-kxlijb .framer-ar7qgq { order: 0; }`,`.framer-YVcpB.framer-v-11ob9oj.hover.framer-9o7ndm, .framer-YVcpB.framer-v-kxlijb.hover.framer-9o7ndm { padding: 8px; }`,...N,`.framer-YVcpB[data-border="true"]::after, .framer-YVcpB [data-border="true"]::after { content: ""; border-width: var(--border-top-width, 0) var(--border-right-width, 0) var(--border-bottom-width, 0) var(--border-left-width, 0); border-color: var(--border-color, none); border-style: var(--border-style, none); width: 100%; height: 100%; position: absolute; box-sizing: border-box; left: 0; top: 0; border-radius: inherit; corner-shape: inherit; pointer-events: none; }`],`framer-YVcpB`),Y.displayName=`Button`,Y.defaultProps={height:32,width:112},E(Y,{variant:{options:[`ubuftqAhL`,`ypBdqWJVj`,`f_D_QmORM`],optionTitles:[`Default`,`Dark Button`,`White Button`],title:`Variant`,type:D.Enum},cUOC4w3WT:{title:`Click`,type:D.EventHandler},zt8ifGc_Q:{title:`Link`,type:D.Link},errt8torn:{defaultValue:`Contact`,displayTextArea:!1,title:`Title`,type:D.String},onerrt8tornChange:{changes:`errt8torn`,type:D.ChangeHandler},OY8OQlhvY:{defaultValue:!0,title:`Show Icon`,type:D.Boolean},onOY8OQlhvYChange:{changes:`OY8OQlhvY`,type:D.ChangeHandler}}),re(Y,[{explicitInter:!0,fonts:[{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0460-052F, U+1C80-1C88, U+20B4, U+2DE0-2DFF, U+A640-A69F, U+FE2E-FE2F`,url:`../images/5vvr9vy74if2i6bqbjvbw7sy1pq.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0301, U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116`,url:`../images/eor0mi4hntlgwnn9if640ezzxco.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+1F00-1FFF`,url:`../images/y9k9qrlzaqio88klkmbd8vomqc.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0370-03FF`,url:`../images/oyrd2tbibpvojxiihnlooxny9m.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF`,url:`../images/jeywfuapfzhqheg8u5gtpdz7wq.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2070, U+2074-207E, U+2080-208E, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD`,url:`../images/grgckwrn6d3uz8ewclhzxwefc4.woff2`,weight:`400`},{cssFamilyName:`Inter`,source:`framer`,style:`normal`,uiFamilyName:`Inter`,unicodeRange:`U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB`,url:`../images/b6y37fthzealdunqhicbt6futy.woff2`,weight:`400`}]},...R,...T(P)],{supportsExplicitInterCodegen:!0})}));function ge(){let e=i(null),t=i(null);return s(()=>{if(!e.current)return;let n=k.context(()=>{t.current=k.to(e.current,{rotation:360,duration:3,ease:`none`,repeat:-1,delay:.5,paused:!0}),F.create({trigger:e.current,start:`top bottom`,onEnter:()=>t.current?.resume(),onLeave:()=>t.current?.pause(),onEnterBack:()=>t.current?.resume(),onLeaveBack:()=>t.current?.pause()})},e);return()=>n.revert()},[]),{ref:e}}function _e(){let e=i(null),t=i(null);return s(()=>{if(!e.current)return;let n=k.context(()=>{t.current=k.to(e.current,{rotation:-360,duration:3,ease:`none`,repeat:-1,delay:.5,paused:!0}),F.create({trigger:e.current,start:`top bottom`,onEnter:()=>t.current?.resume(),onLeave:()=>t.current?.pause(),onEnterBack:()=>t.current?.resume(),onLeaveBack:()=>t.current?.pause()})},e);return()=>n.revert()},[]),{ref:e}}function X(e=0){let t=i(null),n=i(null);return s(()=>{if(!t.current)return;let r=k.context(()=>{k.set(t.current,{scale:0}),n.current=k.to(t.current,{scale:1,duration:1,delay:e,ease:`power2.inOut`,repeat:-1,yoyo:!0,paused:!0}),F.create({trigger:t.current,start:`top bottom`,onEnter:()=>n.current?.resume(),onLeave:()=>n.current?.pause(),onEnterBack:()=>n.current?.resume(),onLeaveBack:()=>n.current?.pause()})},t);return()=>r.revert()},[e]),{ref:t}}function ve(){return X(0)}function ye(){return X(.1)}function be(){return X(.2)}function xe(){return X(.3)}function Se(){let e=i(null),t=i(null);return s(()=>{if(!e.current)return;let n=k.context(()=>{let n=k.timeline({repeat:-1,paused:!0});n.to(e.current,{rotation:-15,duration:.2,ease:`power2.out`}).to(e.current,{rotation:360,duration:.7,ease:`power2.in`}).to(e.current,{rotation:367,duration:.2,ease:`power2.out`}).to(e.current,{rotation:360,duration:.2,ease:`power2.out`}).set(e.current,{rotation:0}).to({},{duration:4}),t.current=n,F.create({trigger:e.current,start:`top bottom`,onEnter:()=>t.current?.resume(),onLeave:()=>t.current?.pause(),onEnterBack:()=>t.current?.resume(),onLeaveBack:()=>t.current?.pause()})},e);return()=>n.revert()},[]),{ref:e}}function Ce(e){return t=>{let a=i(null),o=g(a),s=h(0),c=h(0),l=h(1),d=v(s,{damping:40,stiffness:300}),f=v(c,{damping:40,stiffness:300}),p=v(l,{damping:20,stiffness:300}),m=n!==void 0&&n.matchMedia(`(pointer: coarse)`).matches;return r(()=>{if(m)return;let e=e=>{if(!a.current||!o)return;let t=a.current.getBoundingClientRect();s.set((e.clientX-(t.left+t.width/2))*.04),c.set((e.clientY-(t.top+t.height/2))*.04)};return document.addEventListener(`mousemove`,e),()=>document.removeEventListener(`mousemove`,e)},[o,m]),r(()=>{let e=b(l,[1,.15,1],{duration:.3,repeat:1/0,repeatDelay:2+Math.random()*2,ease:`easeInOut`});return()=>e.stop()},[]),u(e,{...t,ref:a,style:{x:m?0:d,y:m?0:f,scaleY:p,transformOrigin:`center`}})}}function Z(e){return n=>(t(O),u(e,{...n,...ge(n)}))}function Q(e){return n=>(t(O),u(e,{...n,..._e(n)}))}function we(e){return n=>(t(O),u(e,{...n,...X(n)}))}function $(e){return n=>(t(O),u(e,{...n,...ve(n)}))}function Te(e){return n=>(t(O),u(e,{...n,...ye(n)}))}function Ee(e){return n=>(t(O),u(e,{...n,...be(n)}))}function De(e){return n=>(t(O),u(e,{...n,...xe(n)}))}function Oe(e){return n=>(t(O),u(e,{...n,...Se(n)}))}var ke=e((()=>{o(),d(),p(),A(),pe(),x(),C(),k.registerPlugin(F),Z.displayName=`RotateLoop`,Q.displayName=`RotateReverseLoop`,we.displayName=`createScaleLoop`,$.displayName=`ScaleLoop0`,Te.displayName=`ScaleLoop1`,Ee.displayName=`ScaleLoop2`,De.displayName=`ScaleLoop3`,Oe.displayName=`IllusCTA`}));export{Q as a,Ee as c,he as d,I as f,Z as i,De as l,Oe as n,$ as o,me as p,Ce as r,Te as s,ke as t,Y as u};
//# sourceMappingURL=Loop.Do7g2xKB.mjs.map