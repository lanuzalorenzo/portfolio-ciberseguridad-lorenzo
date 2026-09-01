namespace EcommerceApi.Models;

public class Order
{
    public int Id { get; set; }
    public DateTime CreatedAt { get; set; }
    public List<int> ProductIds { get; set; } = new List<int>();
    public decimal Total { get; set; }
}
