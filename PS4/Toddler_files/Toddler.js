requirejs.config( { baseUrl : "js" });
requirejs(["edu/stanford/cs/csdemo/toddler"],
          function(toddler) { toddler.Toddler.main([]); });
