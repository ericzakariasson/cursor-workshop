using Xunit;
using Newtonsoft.Json;

public class PersonTests
{
    [Fact]
    public void SerializePersonToJson_ShouldWork()
    {
        var person = new { Name = "Eric", Age = 99 };
        var json = JsonConvert.SerializeObject(person);
        
        Assert.Equal("{\"Name\":\"Eric\",\"Age\":99}", json);
    }
} 