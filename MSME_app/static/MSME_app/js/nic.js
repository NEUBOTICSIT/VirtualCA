

//var listA = [{name:'01 - 1Crop and animal production, hunting and related service activities', value:'01 - Crop and animal production, hunting and related service activities'}, {name:'05-Mining and Quarring', value:'05-Mining and Quarring'}, {name:'06- Extraction of crude petroleum and natural gas', value:'06- Extraction of crude petroleum and natural gas'},{name:'07-Mining of iron ores',value:'07-Mining of iron ores'}];
//
//var listB = [{name:'Studio 400-600 sq ft', value:'Studio 400-600 sq ft'}, {name:'Studio Alcove 600-700 sq ft', value:'Studio Alcove 600-700 sq ft'}];
//
//var listC = [{name:'hello', value:'hello'}, {name:'abc', value:'abc'}];
//
//  $(document).ready( function() {
//      $("input[name='chk']").on('change',function() {
//
//          if($(this).is(':checked') && $(this).val() == '1')
//          {
//            $('#2_Digit').empty()
//            $.each(listA, function(index, value) {
//             $('#2_Digit').append('<option value="'+value.value+'">'+value.name+'</option>');
//            });
//          }
//          else if($(this).is(':checked') && $(this).val() == '2')
//          {
//            $('#2_Digit').empty()
//            $.each(listB, function(index, value) {
//             $('#2_Digit').append('<option value="'+value.value+'">'+value.name+'</option>');
//            });
//          }
//
//
//           else if($(this).is(':checked') && $(this).val() == '3')
//          {
//            $('#2_Digit').empty()
//            $.each(listC, function(index, value) {
//             $('#2_Digit').append('<option value="'+value.value+'">'+value.name+'</option>');
//            });
//          }
//          else
//          {
//
//          }
//
//    });
// });








var Trading = {
  "45-Wholesale and retail trade and repair of motor vehicles and motorcycles": {
    "4510-Sale of motor vehicles": ["45101-Wholesale and retail sale of new vehicles (passenger motor vehicles, ambulances, minibuses, jeeps, trucks, trailers and semi-trailers)", "45102-Wholesale and retail sale of used motor vehicles"],
    "4520-Maintenance and repair of motor vehicles": ["45200-Maintenance and repair of motor vehicles"],
    "4530-Sale of motor vehicle parts and accessories": ["45300-Sale of motor vehicle parts and accessories"],
    "4540-Sale, maintenance and repair of motorcycles and related parts and Accessories": ["45401-Wholesale or retail sale of new motorcycles, mopeds, scooters and three wheelers","45402-Wholesale or retail sale of parts and accessories of motorcycles, mopeds, scooters and three wheelers","45403-Maintenance and repair of motor cycles, mopeds, scooters and three wheelers"]


  },
  "46-Wholesale trade, except of motor vehicles and motorcycles": {
    "4610-Wholesale on a fee or contract basis": ["46101-Activities of commission agents, brokers dealing in wholesale trade of agricultural raw material, live animals, food, beverages, intoxicants and textiles", "46102-Activities of commission agents dealing in wholesale trade in wood, paper, skin, leather and fur, fuel, petroleum products, chemicals, perfumery and cosmetics, glass, minerals, ores and metals", "46103-Activities of commission agents dealing in wholesale trade in machinery & equipment, other than transport machinery","46104-Activities of other commission agents n.e.c. (including commission agents working in emerging areas for wholesale trade"],
    "4620-Wholesale of agricultural raw materials and live animals": ["46201-Wholesale of cereals & pulses", "46202-Wholesale of un-manufactured tobacco, paan (betel leaf), opium, ganja, cinchona etc", "46203-Wholesale of live animals and poultry","46204-Wholesale of straw, fodder & other animal/poultry feed","46205-Wholesale of flowers and plants","46206-Wholesale of hides, skins and leather","46207-Wholesale of oilseed oleaginous fruits","46208-Wholesale of sugarcane","46209-Whole sale of other agriculture raw materials n.e.c"],
    "4630-Wholesale of food, beverages and tobacco": ["46301-Wholesale of fruits & vegetables", "46302-Wholesale of raw milk & dairy products", "46303-Wholesale of meat, fish & eggs","46304-Wholesale of confectionery, bakery products and beverages other than intoxicants","46305-Wholesale of edible oils, fats, sugar and processed/manufactured spices etc.","46306-Wholesale of tea, coffee & cocoa","46207-Wholesale of manufactured tobacco & tobacco products","46208-Wholesale of intoxicants like wines and liquors","46209-Wholesale of other basic/manufactured food stuffs n.e.c."],
    "4641-Wholesale of textiles, clothing and footwear": ["46411-Wholesale of textiles, fabrics, yarn, household linen, articles of clothing, floor coverings and tapestry, sports clothes", "46412-Wholesale of umbrella and clothing accessories", "46413-Wholesale of footwear","46419-Wholesale of other clothing items n.e.c., bakery products and beverages other than intoxicants"],
    "4649-Wholesale of other household goods": ["46491-Wholesale of toiletry, perfumery and cosmetics, fabrics, yarn, household linen, articles of clothing, floor coverings and tapestry, sports clothes", "46492-Wholesale of metal, porcelain and glass utensils; crockery and chinaware", "46493-Wholesale of furniture and fixtures","46494-Wholesale of watches, clocks and optical goods","46495-Wholesale of recorded audio or video tapes, CDs and DVDs","46496-Wholesale of paper and other stationery items; books, magazines and newspapers","46497-Wholesale of pharmaceutical and medical goods","46498-Wholesale of precious metals and jewellery","46499-Wholesale of other households goods, n.e.c. [Includes wholesale of household equipment and appliances, n.e.c; photographic equipment, games, toys and sports goods (also includes bicycles, cycle rickshaw, tonga & other non-mechanised vehicles); leather goods and travel accessories; cleaning materials etc.]"],
    "4651-Wholesale of computers, computer peripheral equipment and software": ["46511-Wholesale of computers and computer peripheral equipment ", "46512-Wholesale of software"],
    "4652-Wholesale of electronic and telecommunications equipment and parts": ["46521-Wholesale of electronic valves and tubes, semiconductor devices, microchips, integrated circuits and printed circuits ", "46522-Wholesale of radio, television and other consumer electronics including CD/ DVD players and recorders","46523-Wholesale of blank audio and video tapes and diskettes, magnetic and optical disks (CDs, DVDs) and parts","46524-Wholesale of telephone, mobile phone and communications equipment and parts","46529-Wholesale of other electronic equipments and parts thereof"],
    "4653-Wholesale of agricultural machinery, equipment and supplies": ["46531- Wholesale of tractors used in agriculture and forestry", "46532-Wholesale of ploughs, manure spreaders, seeders, harvesters, threshers","46533-Wholesale of milking machines, poultry-keeping machines, bee-keeping machines","46539-Wholesale of other agriculture machinery n.e.c."],
    "4659-Wholesale of other machinery and equipment": ["46591- Wholesale of office machinery and equipment, except computers and computer peripheral equipment", "46592-Wholesale of transport equipment except motor vehicles, motorcycles and bicycles","46593-Wholesale of electrical machinery, equipment and supplies, n.e.c.","46594-Wholesale of construction and civil engineering machinery and equipment","46595-Wholesale of machinery and equipment for the textile, wood and metal industries etc.","46596-Wholesale of scientific, medical and surgical machinery and equipment","46599-Wholesale of other machinery, equipment and supplies n.e.c. including computer-controlled machine tools and computer-controlled sewing and knitting machines"],
    "4661-Wholesale of solid, liquid and gaseous fuels and related products": ["46610-Wholesale of solid, liquid and gaseous fuels and related products"],
    "4662-Wholesale of metals and metal ores": ["46620-Wholesale of metals and metal ores"],
    "4663-Wholesale of construction materials, hardware, plumbing and heating equipment and supplies": ["46631-Wholesale of wood in the rough and products of primary processing of wood","46632-Wholesale of construction materials (sand, gravel etc.)","46633-Wholesale of hardware and sanitary fittings and fixtures and flat glass including tools such as hammers, saws, screwdrivers and other hand tools","46634-Wholesale of paints, varnishes, and lacquers","46639-Wholesale of other construction equipment n.e.c."],
    "4669-Wholesale of waste and scrap and other products n.e.c.": ["46691-Wholesale of industrial chemicals,","46692-Wholesale of fertilizers and agrochemical products","46693-Wholesale of plastic materials in primary forms","46694-Wholesale of rubber","46695-Wholesale of textile fibres etc.","46696-Wholesale of paper in bulk","46697-Wholesale of precious stones","46699-Wholesale of metal and non-metal waste and scrap n.e.c."],
    "4690-Non-specialized wholesale trade": ["46901-Wholesale trade via e-commerce excluding activities of commission agents, liquid and gaseous fuels and related products","46909-Other non-specialised wholesale trade n.e.c."]

  },
   "47-Retail trade, except of motor vehicles and motorcycles": {
    "4711-Retail sale in non-specialized stores with food, beverages or tobacco predominating": ["47110-Retail sale in non-specialized stores with food, beverages or tobacco predominating"],
    "4619-Other retail sale in non-specialized stores": ["47190-Other retail sale in non-specialized stores"],
    "4721-Retail sale of food in specialized stores": ["47211-Retail sale of cereals and pulses, tea, coffee, spices and flour", "47212-Retail sale of fresh or preserved fruit and vegetables", "47213-Retail sale of meat, meat products, poultry products, fish, other seafood and products thereof","46304-Retail sale of bakery products, dairy products and eggs","47215-Retail sale of sugar confectionery and sweetmeat","47219-Retail sale of other food products n.e.c."],
    "4622-Retail sale of beverages in specialized stores": ["47221-Retail sale of alcoholic beverages not consumed on the spot","47222-Retail sale of non-alcoholic beverages including icecream not for consumption on the premises"],
    "4623-Retail sale of tobacco products in specialized stores": ["47230- Retail sale of tobacco products in specialized stores"],
    "4630-Retail sale of automotive fuel in specialized stores": ["47300-Retail sale of automotive fuel in specialized stores [includes the activity of petrol filling stations."],
    "4641-Retail sale of computers, peripheral units, software and telecommunications equipment in specialized stores": ["47411-Retail sale of computers and computer peripherals","47412-Retail sale of video games","47413-Retail sale of non-customized software","47414-Retail sale of telecommunication equipment"],
    "4642-Retail sale of audio and video equipment in specialized stores": ["47420- Retail sale of audio and video equipment in specialized stores"],
    "4651-Retail sale of textiles in specialized stores": ["47510-Retail sale of textiles in specialized stores"],
    "4652-Retail sale of hardware, paints and glass in specialized stores": ["47521-Retail sale of building material such as bricks, wood, sanitary equipment","47522-Retail sale of hardware including paints, varnishes and lacquers and do-it yourself materials and equipments","47523-Retail sale of glass"],
    "4653-Retail sale of carpets, rugs, wall and floor coverings in specialized stores": ["47531-Retail sale of carpets, rugs, curtains and net curtains","47532-Retail sale of wallpaper and floor coverings"],
    "4659-Retail sale of electrical household appliances, furniture, lighting equipment and other household articles in specialized stores": ["47591-Retail sale of household furniture","47592-Retail sale of household utensils and cutlery, crockery, glassware, china and pottery","47593-Retail sale of gas stoves, cooking/kitchen appliances","47594-Retail sale of refrigerators, washing machines and other electrical/electronic household goods","47595-Retail sale of musical instruments","47599-Retail sale of other household appliances n.e.c. ( security systems, such as locking devices, safes, and vaults, without installation or maintenance services etc. , wooden, cork and wickerwork goods, sewing and knitting machine and other household utensils and durables n.e.c.)"],
    "4661-Retail sale of books, newspapers and stationary in specialized stores": ["47611-Retail sale of books of all kinds","47612-Retail sale of newspapers and magazines","47613-Retail sale of stationery office supplies such as pens, pencils, paper etc."],
    "4662-Retail sale of music and video recordings in specialized stores": ["47620-Retail sale of music and video recordings in specialized stores"],
    "4663-Retail sale of sporting equipment in specialized stores": ["47630-Retail sale of sporting equipment in specialized stores"],
    "4664-Retail sale of games and toys in specialized stores": ["47640-Retail sale of games and toys in specialized stores"],
    "4671-Retail sale of clothing, footwear and leather articles in specialized stores": ["47711-Retail sale of readymade garments, hosiery goods, other articles of clothing and clothing accessories such as gloves, ties, braces etc.","47712-Retail sale of articles of fur and artificial fur","47713-Retail sale of footwear","47714-Retail sale of leather goods and travel accessories of leather and leather substitutes"],
    "4672-Retail sale of pharmaceutical and medical goods, cosmetic and toilet articles in specialized stores": ["47721-Retail sale of pharmaceuticals, medical and orthopaedic goods and toilet articles","47722-Retail sale of perfumery and cosmetic articles"],
    "4673-Other retail sale of new goods in specialized stores": ["47731-Retail sale of photographic, optical and precision equipment","47732-Retail sale of watches and clocks","47733-Retail sale of jewellery and immitation jewellery","47734-Retail sale of flowers, plants, pet animals and pet food","47735-Retail sale of souvenirs, craftwork and religious articles, stamps and coins","47736-Retail sale of household fuel oil, bottled gas, coal and fuel wood","47737-Retail sale of seeds, fertilisers, pesticides, machinery equipments and hand tools","47738-Activities of commercial art galleries","47739-Other retail sale of new goods in specialized stores n.e.c (weapons and ammunition, non food products)"],
    "4674-Retail sale of second-hand goods": ["47740-Retail sale of second-hand goods"],
    "4681-Retail sale via stalls and markets of food, beverages and tobacco products": ["47810-Retail sale via stalls and markets of food, beverages and tobacco products"],
    "4682-Retail sale via stalls and markets of textiles, clothing and footwear": ["47820-Retail sale via stalls and markets of textiles, clothing and footwear"],
    "4689-Retail sale via stalls and markets of other goods": ["47890-Retail sale via stalls and markets of other goods"],
    "4691-Retail sale via mail order houses or via Internet": ["47911-Retail sale via mail order houses","47912-Retail sale via e-commerce"],
    "4699-Other retail sale not in stores, stalls or markets": ["47990-Other retail sale not in stores, stalls or markets"],

  }
}
window.onload = function() {
  var nic_2_digit = document.getElementById("2_Digit");
  var nic_4_digit = document.getElementById("4_Digit");
  var nic_5_digit = document.getElementById("5_Digit");
  for (var x in Trading) {
    nic_2_digit.options[nic_2_digit.options.length] = new Option(x, x);
  }
  nic_2_digit.onchange = function() {
    //empty Chapters- and Topics- dropdowns
    nic_5_digit.length = 1;
    nic_4_digit.length = 1;
    //display correct values
    for (var y in Trading[this.value]) {
      nic_4_digit.options[nic_4_digit.options.length] = new Option(y, y);
    }
  }
  nic_4_digit.onchange = function() {
    //empty Chapters dropdown
    nic_5_digit.length = 1;
    //display correct values
    var z = Trading[nic_2_digit.value][this.value];
    for (var i = 0; i < z.length; i++) {
      nic_5_digit.options[nic_5_digit.options.length] = new Option(z[i], z[i]);
    }
  }
}
