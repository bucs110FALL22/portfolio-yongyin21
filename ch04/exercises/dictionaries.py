article = ("Then-President Donald Trump nearly fired his daughter Ivanka Trump and son-in-law Jared Kushner from the White House via tweet, according to a new book from New York Times reporter Maggie Haberman. Trump raised the prospect of firing Ivanka Trump and Kushner, who were both senior White House aides, during meetings with then-chief of staff John Kelly and then-White House counsel Don McGahn, Haberman writes. At one point, he was about to tweet that his daughter and son-in-law were leaving the White House – but he was stopped by Kelly, who told Trump he had to speak with them directly first.Trump never had such a conversation – one of numerous instances where he avoided interpersonal conflict – and Ivanka Trump and Kushner remained at the White House throughout Trump’s presidency. Still, Trump often diminished Kushner, mocking him as effete, Haberman writes."

)

substitutions = {
   "White House":"Pit of Despair",
    "allegedly":"totally",
    "bill":"snap I didn’t screenshot",
    "official":"puppy",
    "congressional":"spaaaaace",
    "republican":"piano accordionist",
    "democrat":"chromatic button accordionist",
    "senator": "magical wizard",
    "representative": "unmagical wizard",
    "secretary":"eating champion",
    "leaders":"goblins",
    "washington":"Mount Doom",
    "President": "you know, the guy"

}

for key, value in substitutions.items():
  article = article.replace(key, value)

print(article)