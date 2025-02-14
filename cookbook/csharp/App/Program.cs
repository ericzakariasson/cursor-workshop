using Newtonsoft.Json;

var person = new { Name = "Eric", Age = 99 };
var json = JsonConvert.SerializeObject(person);
Console.WriteLine(json);
